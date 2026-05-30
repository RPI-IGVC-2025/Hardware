#include <FastLED.h>
#define pinNumber 16
int pinState = 0;

#define NUM_LEDS 60
#define DATA_PIN 3
CRGB leds[NUM_LEDS];

void setup() {
  pinMode(pinNumber, INPUT);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);

  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB::Yellow;
  }
  FastLED.show();

}
 
void loop() {
  if (pinState != digitalRead(pinNumber)) {
    pinState = !pinState;
    if (pinState) {
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = CRGB::Green;
      }
    } else {
      FastLED.clear();
    }
    FastLED.show();
  }
}