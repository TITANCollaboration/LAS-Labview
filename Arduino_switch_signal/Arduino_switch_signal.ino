void setup() {
  pinMode(4, INPUT); // Set pin 4 (ICP1) as an input
  pinMode(9, OUTPUT); // Configure the output pin
  digitalWrite(9, HIGH); // Set output to HIGH to block the ions
}

void loop() {
  // When a signal from the laser is reciecved:
  if(PIND & (1<<PD4)){
    delayMicroseconds(11);
    // NOP command: __asm__("nop\n\t"); wait one clock cycle (62.5ns)
    // Add 8 NOPS extra to correct on-scope to the microsecond
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    // Fractional microseconds below:
    
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    
    PORTB ^= (1 << PORTB5); // Send switch down TTL signal
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    __asm__("nop\n\t");
    PORTB ^= (1 << PORTB5); // Send switch up TTL signal
    delay(1); // Delay for laser signal to return to LOW. Avoids extra trigger. 
  }
}
