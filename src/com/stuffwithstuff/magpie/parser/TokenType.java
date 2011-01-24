package com.stuffwithstuff.magpie.parser;

public enum TokenType {
  // punctuation and grouping
  LEFT_PAREN,
  RIGHT_PAREN,
  LEFT_BRACKET,
  RIGHT_BRACKET,
  LEFT_BRACE,
  RIGHT_BRACE,
  BACKTICK,
  COMMA,
  DOT,
  EQUALS,
  
  // identifiers
  NAME,
  FIELD,      // a record field like "x:"
  OPERATOR,
  TYPE_PARAM, // a type parameter in a pattern like 'T

  // literals
  BOOL,
  INT,
  DOUBLE,
  STRING,
  
  // keywords
  AND,
  ARROW,
  CASE,
  CATCH,
  CLASS,
  DELEGATE,
  EXTEND,
  FN,
  FOR,
  INTERFACE,
  LET,
  MATCH,
  NOTHING,
  OR,
  SET,
  THEN,
  THIS,
  WHILE,
  WITH,
  
  // spacing
  LINE,
  EOF
}
