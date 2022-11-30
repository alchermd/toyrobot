# Improvements

## Separate the parsing and sanitation logic to its own class

I've extracted the `_parse_command` and `_sanitize_input` into their own respective `Parser` and `Sanitizer` classes.
Default instances are also provided as to allow changing of parsers/sanitizers on runtime.

## Update sanitation of the PLACE command

## Handle moving out of bounds

## Allow shorthand directions

## Implement a proper game loop