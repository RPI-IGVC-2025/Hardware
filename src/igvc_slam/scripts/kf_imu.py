import numpy as np

class KalmanFilter:
    """
    Discrete-time linear Kalman Filter (KF).

    System model:
      x_{k+1} = A x_k + B u_k + w_k
      z_k     = H x_k + v_k

    Assumptions:
      w_k ~ N(0, Q), v_k ~ N(0, R), and w_k is independent of v_k.

    Parameters:
      A: State transition matrix.
      B: Control matrix.
      H: Observation matrix.
      Q: Process noise covariance.
      R: Measurement noise covariance.
      x: State estimate.
      x0: Initial state estimate.
      P: Error covariance of the estimate.
         - Diagonal: variance of each state estimate.
         - Off-diagonal: correlation between state errors.
      P0: Initial error covariance.
    """
    def __init__(self, A, B, H, Q, R, x0, P0):
        self.A = A
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0

    def predict(self, u):
        """
        Prediction (time update).

        Notation:
          x_k: true state at time k
          x_k^-: prior estimate at time k
          e_k^- = x_k - x_k^-

        State prediction:
          x_{k+1}^- = A x_k^- + B u_k

        Error propagation:
          e_{k+1}^- = x_{k+1} - x_{k+1}^-
                    = A (x_k - x_k^-) + w_k
                    = A e_k^- + w_k

        Covariance prediction:
          P_{k+1}^- = E[e_{k+1}^- e_{k+1}^{-T}]
                    = E[(A e_k^- + w_k)(A e_k^- + w_k)^T]
                    = A E[e_k^- e_k^{-T}] A^T + E[w_k w_k^T]
                    = A P_k^- A^T + Q
        """
        self.x = np.dot(self.A, self.x) + np.dot(self.B, u)
        self.P = np.dot(self.A, np.dot(self.P, self.A.T)) + self.Q
        return self.x

    def update(self, z):
        """
        Measurement update (correction).

        Notation:
          x_k^+: posterior estimate after using measurement at time k
          e_k^- = x_k - x_k^-
          y_k = z_k - H x_k^-  (innovation)

        Innovation covariance:
          y_k = H e_k^- + v_k
          S_k = E[y_k y_k^T]
              = H E[e_k^- e_k^{-T}] H^T + E[v_k v_k^T]
              = H P_k^- H^T + R
        ------------------------------
        Linear correction:
          x_k^+ = x_k^- + K_k y_k
          e_k^+ = x_k - x_k^+ = e_k^- - K_k y_k

        Substitute y_k:
          e_k^+ = (I - K_k H) e_k^- - K_k v_k

        Posterior covariance:
          P_k^+ = E[e_k^+ e_k^{+T}]
                = (I - K_k H) P_k^- (I - K_k H)^T + K_k R K_k^T

        Optimal K (orthogonality principle: E[e_k^+ y_k^T] = 0):
          E[e_k^- y_k^T] = K_k E[y_k y_k^T]
          P_k^- H^T = K_k S_k
          K_k = P_k^- H^T S_k^{-1}

        Posterior update (result):
          x_k^+ = x_k^- + K_k y_k
          P_k^+ = (I - K_k H) P_k^- (I - K_k H)^T + K_k R K_k^T

        """
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R

        """
        Numerical computation of K:
          K_k = P_k^- H^T S_k^{-1}
          K_k S_k = P_k^- H^T
          Solve for K_k^T using np.linalg.solve:
            S_k^T K_k^T = (P_k^- H^T)^T
            K_k = (K_k^T)^T
        """
        PHt = np.dot(self.P, self.H.T)
        K_T = np.linalg.solve(S.T, PHt.T)
        K = K_T.T

        y = z - np.dot(self.H, self.x)
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.P.shape[0])
        self.P = np.dot(np.dot(I - np.dot(K, self.H), self.P), (I - np.dot(K, self.H)).T) + np.dot(np.dot(K, self.R),K.T)
        return self.x  # Return estimated state after correction.