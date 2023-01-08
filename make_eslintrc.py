#!/usr/bin/env python

import json
import sys


eslint_rules = {
    # Disallow setters without corresponding getters. Default options.
    "accessor-pairs": "error",

    # Enforce consistent line breaks between array brackets. Default options.
    "array-bracket-newline": "warn",

    # Disallow spaces inside array brackets. Default options.
    "array-bracket-spacing": "warn",

    # Require return statements in array method callbacks.
    # checkForEach disallows return statements in Array#forEach.
    "array-callback-return": ["error", {"checkForEach": True}],

    # Enforce consistent line breaks between array elements.
    "array-element-newline": ["warn", "consistent"],

    # Enforce consistent use of braces in arrow functions. Default options.
    "arrow-body-style": "warn",

    # Enforce consistent use of parentheses around arrow function parameters.
    "arrow-parens": ["warn", "as-needed"],

    # Require spacing around the arrow in arrow functions. Default options.
    "arrow-spacing": "warn",

    # Not needed because eslint/no-var disallows all usage of `var`.
    "block-scoped-var": "off",

    # Require spaces inside code blocks. Default options.
    "block-spacing": "warn",

    # See @typescript-eslint/brace-style
    "brace-style": "off",

    # Disabled because @typescript-eslint/naming-convention is more comprehensive.
    "camelcase": "off",

    # Not useful.
    "capitalized-comments": "off",

    # Require class methods to use `this` (otherwise they should be static). Default options.
    "class-methods-use-this": "error",

    # See @typescript-eslint/comma-dangle
    "comma-dangle": "off",

    # See @typescript-eslint/comma-spacing
    "comma-spacing": "off",

    # Require comma-separated lists to have commas at the end of line. Default options.
    "comma-style": "warn",

    # Enforce a maximum cyclomatic complexity. Default options.
    "complexity": "warn",

    # Disallow spaces inside computed property brackets. Default options.
    "computed-property-spacing": "warn",

    # Require return statements to either always or never specify values. Default options.
    "consistent-return": "error",

    # Disabled because @typescript-eslint/no-this-alias disallows aliasing `this`.
    "consistent-this": "off",

    # Require super() calls in constructors. No options.
    "constructor-super": "error",

    # Require consistent brace use and braces around complex blocks.
    "curly": ["warn", "multi-or-nest", "consistent"],

    # Not useful.
    "default-case": "off",

    # Enforce default clauses in switch statements to be last. No options.
    "default-case-last": "error",

    # See @typescript-eslint/default-param-last
    "default-param-last": "off",

    # Enforce consistent line breaks before and after dots.
    "dot-location": ["warn", "property"],

    # See @typescript-eslint/dot-notation
    "dot-notation": "off",

    # Require newline at the end of file. Default options.
    "eol-last": "warn",

    # Require the use of === and !==, except when comparing against a null literal.
    "eqeqeq": ["error", "always", {"null": "ignore"}],

    # Detect errors possibly causing infinite loops. Default options.
    "for-direction": "error",

    # See @typescript-eslint/func-call-spacing
    "func-call-spacing": "off",

    # Require function names to match the name to which they are assigned.
    "func-name-matching": ["warn", "always", {"considerPropertyDescriptor": True}],

    # Require naming function expressions, if a name is not automatically assigned.
    "func-names": ["warn", "as-needed"],

    # Enforce the use of function expressions over function declarations. Default options.
    "func-style": "warn",

    # Enforce consistent line breaks between arguments of a function call.
    "function-call-argument-newline": ["warn", "consistent"],

    # Enforce consistent line breaks inside function parentheses. Default options.
    "function-paren-newline": "warn",

    # Enforce consistent spacing around `*` operators in generator functions.
    "generator-star-spacing": ["warn", "after"],

    # Require return statements in getters. Default options.
    "getter-return": "error",

    # Require setters to immediately follow corresponding getters.
    "grouped-accessor-pairs": ["warn", "getBeforeSet"],

    # Disabled because @typescript-eslint/no-for-in-array disables for-in loops entirely.
    "guard-for-in": "off",

    # Not useful.
    "id-denylist": "off",

    # Not useful.
    "id-length": "off",

    # Not useful.
    "id-match": "off",

    # Disallow line break before an arrow function body. Default options.
    "implicit-arrow-linebreak": "warn",

    # See @typescript-eslint/indent
    "indent": "off",

    # See @typescript-eslint/init-declarations
    "init-declarations": "off",

    # Enforce the consistent use of either double quotes in JSX attributes. Default options.
    "jsx-quotes": "warn",

    # Enforce consistent spacing between keys and values in object literals. Default options.
    "key-spacing": "warn",

    # See @typescript-eslint/keyword-spacing
    "keyword-spacing": "off",

    # Not useful.
    "line-comment-position": "off",

    # Enforce Unix-style newlines. Default options.
    "linebreak-style": "error",

    # Not useful.
    "lines-around-comment": "off",

    # See @typescript-eslint/lines-between-class-members
    "lines-between-class-members": "off",

    # Enforce using logical operator shorthands. Default options.
    "logical-assignment-operators": "warn",

    # Not useful.
    "max-classes-per-file": "off",

    # Enforce a maximum nesting depth of 4. Default options.
    "max-depth": "warn",

    # Enforce a maximum line length, with exceptions for literals.
    "max-len": ["warn", {
      "code": 100,
      "ignoreRegExpLiterals": True,
      "ignoreStrings": True,
      "ignoreTemplateLiterals": True,
    }],

    # Not useful.
    "max-lines": "off",

    # Not useful.
    "max-lines-per-function": "off",

    # Enforce a maximum depth that callbacks can be nested.
    "max-nested-callbacks": ["warn", 5],

    # Not useful.
    "max-params": "off",

    # Not useful.
    "max-statements": "off",

    # Enforce only one statement allowed per line. Default options.
    "max-statements-per-line": "error",

    # Not useful.
    "multiline-comment-style": "off",

    # Enforce consistent line breaks between operands of ternary expressions.
    "multiline-ternary": ["warn", "always-multiline"],

    # Require constructor names to begin with a capital letter. Default options.
    "new-cap": "warn",

    # Require parentheses when invoking a constructor with no arguments. Default options.
    "new-parens": "error",

    # Require a line break after each call in longer method chains. Default options.
    "newline-per-chained-call": "warn",

    # Disallow the use of alert(), confirm(), and prompt(). No options.
    "no-alert": "warn",

    # See @typescript-eslint/no-array-constructor
    "no-array-constructor": "off",

    # Disallow using an async function as a Promise executor. No options.
    "no-async-promise-executor": "error",

    # Disallow await inside of loops (should probably use Promise.all()). No options.
    "no-await-in-loop": "error",

    # Not useful.
    "no-bitwise": "off",

    # Disallow the use of arguments.caller or arguments.callee. No options.
    "no-caller": "error",

    # Disallow declarations in case clauses. No options.
    "no-case-declarations": "error",

    # Disallow reassigning class members. No options.
    "no-class-assign": "error",

    # Disallow comparing against -0. No options.
    "no-compare-neg-zero": "error",

    # Disallow assignments in conditional expressions, except inside parentheses. Default options.
    "no-cond-assign": "error",

    # Not useful.
    "no-confusing-arrow": "off",

    # Not useful.
    "no-console": "off",

    # Disallow reassigning const variables. No options.
    "no-const-assign": "error",

    # Disallow expressions where the operation doesn't affect the value. No options.
    "no-constant-binary-expression": "error",

    # Disallow constant expressions in conditions. Default options.
    "no-constant-condition": "error",

    # Disallow returning a value from a constructor. No options.
    "no-constructor-return": "error",

    # Not useful.
    "no-continue": "off",

    # Disallow control characters in regular expressions. No options.
    "no-control-regex": "error",

    # Disallow the use of `debugger`. No options.
    "no-debugger": "error",

    # Disallow deleting variables. No options.
    "no-delete-var": "error",

    # Not useful.
    "no-div-regex": "off",

    # Disallow duplicate arguments in function definitions. No options.
    "no-dupe-args": "error",

    # See @typescript-eslint/no-dupe-class-members
    "no-dupe-class-members": "off",

    # Disallow duplicate conditions in if-else-if chains. No options.
    "no-dupe-else-if": "error",

    # Disallow duplicate keys in object literals. No options.
    "no-dupe-keys": "error",

    # Disallow duplicate case labels. No options.
    "no-duplicate-case": "error",

    # Disallow duplicate module imports.
    "no-duplicate-imports": "warn",

    # Disallow useless else blocks after return statements in if statements. Default options.
    "no-else-return": "warn",

    # Disallow empty block statements. Default options.s
    "no-empty": "error",

    # Disallow empty character classes in regular expressions. No options.
    "no-empty-character-class": "error",

    # See @typescript-eslint/no-empty-function
    "no-empty-function": "off",

    # Disallow empty destructuring patterns. No options.
    "no-empty-pattern": "error",

    # Disallow empty static blocks. No options.
    "no-empty-static-block": "error",

    # Not useful.
    "no-eq-null": "off",

    # Disallow the use of eval(). Default options.
    "no-eval": "error",

    # Disallow reassigning exceptions in catch clauses. No options.
    "no-ex-assign": "error",

    # Disallow extending native types. Default options.
    "no-extend-native": "error",

    # Disallow unnecessary calls to Function.bind(). No options.
    "no-extra-bind": "error",

    # Disallow unnecessary boolean casts.
    "no-extra-boolean-cast": ["error", {"enforceForLogicalOperands": True}],

    # Disallow unnecessary labels. No options.
    "no-extra-label": "error",

    # Disallow unnecessary parentheses. Default options.
    "no-extra-parens": "off",

    # See @typescript-eslint/no-extra-semi
    "no-extra-semi": "off",

    # Disallow fallthrough of case statements. Default options.
    "no-fallthrough": "warn",

    # Disallow leading or trailing decimal points in numeric literals. No options.
    "no-floating-decimal": "warn",

    # Disallow reassigning function declarations. No options.
    "no-func-assign": "error",

    # Disallow assignments to native objects or read-only global variables. Default options.
    "no-global-assign": "error",

    # Disallow shorthand type conversions. Default options.
    "no-implicit-coercion": "warn",

    # Disallow declarations in the global scope. Default options.
    "no-implicit-globals": "error",

    # See @typescript-eslint/no-implied-eval
    "no-implied-eval": "off",

    # Disallow assigning to imported bindings. No options.
    "no-import-assign": "error",

    # Not useful.
    "no-inline-comments": "off",

    # Disallow function and var declarations in nested blocks.
    "no-inner-declarations": ["error", "both"],

    # Disallow invalid regular expression strings in RegExp constructors. Default options.
    "no-invalid-regexp": "error",

    # See @typescript-eslint/no-invalid-this
    "no-invalid-this": "off",

    # Disallow irregular whitespace.
    "no-irregular-whitespace": ["warn", {"skipStrings": False}],

    # Disallow the use of the __iterator__ property. No options.
    "no-iterator": "error",

    # Disallow labels that share a name with a variable. No options.
    "no-label-var": "error",

    # Only allow labels pointing to loop statements.
    "no-labels": ["error", {"allowLoop": True}],

    # Disallow unnecessary nested blocks. No options.
    "no-lone-blocks": "error",

    # Disallow if statements as the only statement in else blocks. No options.
    "no-lonely-if": "error",

    # See @typescript-eslint/no-loop-func
    "no-loop-func": "off",

    # See @typescript-eslint/no-loss-of-precision
    "no-loss-of-precision": "off",

    # See @typescript-eslint/no-magic-numbers
    "no-magic-numbers": "off",

    # Disallow characters which are made with multiple code points in character class syntax.
    # No options.
    "no-misleading-character-class": "error",

    # Disallow mixed binary operators without parentheses. Default options.
    "no-mixed-operators": "warn",

    # Not needed because the eslint/no-tabs disallows all tabs.
    "no-mixed-spaces-and-tabs": "off",

    # Disallow use of chained assignment expressions. Default options.
    "no-multi-assign": "error",

    # Disallow multiple spaces in a row, except when preceding an end-of-line comment.
    "no-multi-spaces": ["warn", {"ignoreEOLComments": True}],

    # Not useful.
    "no-multi-str": "off",

    # Disallow more than 2 empty lines in a row.
    "no-multiple-empty-lines": ["warn", {"max": 2, "maxBOF": 0, "maxEOF": 0}],

    # Not useful.
    "no-negated-condition": "off",

    # Disallow nested ternary expressions. No options.
    "no-nested-ternary": "warn",

    # Disallow `new` operators outside of assignments or comparisons. No options.
    "no-new": "error",

    # Disallow passing strings to `Function` in an eval-like fashion. No options.
    "no-new-func": "error",

    # Disallow new operators with global non-constructor functions. No options.
    "no-new-native-nonconstructor": "error",

    # Disallow `new Object()` usage. No options.
    "no-new-object": "error",

    # Disallow `new` operators with the `Symbol` object. No options.
    "no-new-symbol": "error",

    # Disallow `new` operators with the `String`, `Number`, and `Boolean` objects. No options.
    "no-new-wrappers": "error",

    # Disallow \8 and \9 escape sequences in string literals. No options.
    "no-nonoctal-decimal-escape": "error",

    # Disallow calling global object properties as functions. No options.
    "no-obj-calls": "error",

    # Disallow octal literals (010, not 0o10). No options.
    "no-octal": "error",

    # Disallow octal escape sequences in string literals. No options.
    "no-octal-escape": "error",

    # Disallow reassigning function parameters. Default options.
    "no-param-reassign": "error",

    # Disallow the unary operators `++` and `--`. Default options.
    "no-plusplus": "warn",

    # Disallow returning values from Promise executor functions. No options.
    "no-promise-executor-return": "error",

    # Disallow the use of the __proto__ property. No options.
    "no-proto": "error",

    # Disallow calling some Object.prototype methods directly on objects. No options.
    "no-prototype-builtins": "error",

    # See @typescript-eslint/no-redeclare
    "no-redeclare": "off",

    # Disallow consecutive spaces in regular expressions. No options.
    "no-regex-spaces": "warn",

    # Not useful.
    "no-restricted-exports": "off",

    # Not useful.
    "no-restricted-globals": "off",

    # Not useful.
    "no-restricted-imports": "off",

    # Not useful.
    "no-restricted-properties": "off",

    # Not useful.
    "no-restricted-syntax": "off",

    # Disallow assignment operators in return statements, unless in parentheses. Default options.
    "no-return-assign": "error",

    # See @typescript-eslint/return-await
    "no-return-await": "off",

    # Not useful.
    "no-script-url": "off",

    # Disallow assignments where both sides are exactly the same. Default options.
    "no-self-assign": "error",

    # Disallow comparisons where both sides are exactly the same. No options.
    "no-self-compare": "error",

    # Disallow comma operators, unless in parentheses. Default options.
    "no-sequences": "warn",

    # Disallow returning values from setters. No options.
    "no-setter-return": "error",

    # See @typescript-eslint/no-shadow
    "no-shadow": "off",

    # Disallow identifiers from shadowing restricted names. No options.
    "no-shadow-restricted-names": "error",

    # Disallow sparse arrays. No options.
    "no-sparse-arrays": "error",

    # Disallow all tabs. Default options.
    "no-tabs": "error",

    # Not useful.
    "no-template-curly-in-string": "off",

    # Not useful.
    "no-ternary": "off",

    # Disallow `this` and `super` before calling `super()` in constructors. No options.
    "no-this-before-super": "error",

    # See @typescript-eslint/no-throw-literal
    "no-throw-literal": "off",

    # Disallow trailing whitespace at the end of lines. Default options.
    "no-trailing-spaces": "error",

    # Disallow the use of undeclared variables.
    "no-undef": ["error", {"typeof": True}],

    # Disallow initializing variables to undefined. No options.
    "no-undef-init": "error",

    # Not needed because of eslint/no-global-assign and eslint/no-shadow-restricted-names.
    "no-undefined": "off",

    # Disabled because there is no option to allow underscore suffixes,
    # which are useful to avoid clashes with keywords.
    "no-underscore-dangle": "off",

    # Disallow confusing multiline expressions. No options.
    "no-unexpected-multiline": "warn",

    # Disallow unmodified loop conditions. No options.
    "no-unmodified-loop-condition": "error",

    # Disallow ternary operators when simpler alternatives exist.
    "no-unneeded-ternary": ["warn", {"defaultAssignment": False}],

    # Disallow unreachable code after return, throw, continue, and break statements. No options.
    "no-unreachable": "warn",

    # Disallow loops with a body that allows only one iteration. Default options.
    "no-unreachable-loop": "error",

    # Disallow control flow statements in `finally` blocks. No options.
    "no-unsafe-finally": "error",

    # Disallow negating the left operand of `in` and `instanceof`.
    "no-unsafe-negation": "error",

    # Disallow use of optional chaining where the `undefined` value is not allowed.
    "no-unsafe-optional-chaining": ["error", {"disallowArithmeticOperators": True}],

    # See @typescript-eslint/no-unused-expressions
    "no-unused-expressions": "off",

    # Disallow unused labels. No options.
    "no-unused-labels": "error",

    # Disallow unused private class members. No options.
    "no-unused-private-class-members": "error",

    # See @typescript-eslint/no-unused-vars
    "no-unused-vars": "off",

    # See @typescript-eslint/no-use-before-define
    "no-use-before-define": "off",

    # Disallow useless backreferences in regular expressions. No options.
    "no-useless-backreference": "error",

    # Disallow unnecessary calls to .call() and .apply(). No options.
    "no-useless-call": "warn",

    # Disallow unnecessary catch clauses. No options.
    "no-useless-catch": "warn",

    # Disallow unnecessary computed property keys in objects and classes.
    "no-useless-computed-key": ["warn", {"enforceForClassMembers": True}],

    # Disallow unnecessary concatenation of literals or template literals. No options.
    "no-useless-concat": "warn",

    # See @typescript-eslint/no-useless-constructor
    "no-useless-constructor": "off",

    # Disallow unnecessary escape characters. No options.
    "no-useless-escape": "error",

    # Disallow renaming to the same name in import, export, and destructuring. Default options.
    "no-useless-rename": "warn",

    # Disallow redundant return statements. No options.
    "no-useless-return": "warn",

    # Require `let` or `const` instead of `var`. No options.
    "no-var": "error",

    # Disallow `void` expressions.
    "no-void": ["error", {"allowAsStatement": True}],

    # Not useful.
    "no-warning-comments": "off",

    # Disallow whitespace before properties. No options.
    "no-whitespace-before-property": "warn",

    # Disallow `with` statements. No options.
    "no-with": "error",

    # Require a line break before a single-line control flow block.
    "nonblock-statement-body-position": ["warn", "below"],

    # Enforce consistent line breaks in object literals and destructuring assignments.
    # Default options.
    "object-curly-newline": "warn",

    # See @typescript-eslint/object-curly-spacing
    "object-curly-spacing": "off",

    # Enforce placing object properties on separate lines, or all on one line.
    "object-property-newline": ["warn", {"allowAllPropertiesOnSameLine": True}],

    # Enforce use of method and property shorthand syntax for object literals. Default options.
    "object-shorthand": "warn",

    # Require each variable declaration to have its own `let` or `const` keyword.
    "one-var": ["warn", "never"],

    # Enforce consistent line breaks around variable initializations. Default options.
    "one-var-declaration-per-line": "warn",

    # Enforce use of assignment operator shorthands where possible. Default options.
    "operator-assignment": "warn",

    # Require line breaks in multiline expressions to be placed before the operator.
    "operator-linebreak": ["warn", "before"],

    # Disallow empty lines at the beginning and ending of blocks.
    "padded-blocks": ["warn", "never"],

    # See @typescript-eslint/padding-line-between-statements
    "padding-line-between-statements": "off",

    # Require using arrow functions for callbacks not containing `this`. Default options.
    "prefer-arrow-callback": "warn",

    # Require `const` declarations for variables that are never reassigned after declared.
    # Default options.
    "prefer-const": "error",

    # Require destructuring from arrays and objects. Default options.
    "prefer-destructuring": "warn",

    # Disallow the use of `Math.pow` in favor of the `**` operator. No options.
    "prefer-exponentiation-operator": "warn",

    # Enforce using named capture group in regular expression. No options.
    "prefer-named-capture-group": "warn",

    # Disallow `parseInt()` and `Number.parseInt()` in favor of 0b/0o/0x literals. No options.
    "prefer-numeric-literals": "warn",

    # Disallow use of `Object.prototype.hasOwnProperty.call()`. No options.
    "prefer-object-has-own": "warn",

    # Disallow using `Object.assign()` with an object literal as the first argument. No options.
    "prefer-object-spread": "warn",

    # Require using Error objects as Promise rejection reasons. Default options.
    "prefer-promise-reject-errors": "error",

    # Disallow use of `new RegExp()` in favor of regular expression literals.
    "prefer-regex-literals": ["warn", {"disallowRedundantWrapping": True}],

    # Enforce use of rest parameters instead of `arguments`. No options.
    "prefer-rest-params": "error",

    # Require spread operators instead of `.apply()`. No options.
    "prefer-spread": "warn",

    # Require template literals instead of string concatenation. No options.
    "prefer-template": "warn",

    # Enforce consistent use of quotes around object literal property names.
    "quote-props": ["warn", "consistent-as-needed"],

    # See @typescript-eslint/quotes
    "quotes": "off",

    # Require providing the radix argument when using `parseInt()`. Default options.
    "radix": "error",

    # Disallow assignments that can lead to race conditions due to usage of `await` or `yield`.
    # Default options.
    "require-atomic-updates": "error",

    # See @typescript-eslint/require-await
    "require-await": "off",

    # Enforce use of `u` flag with regular expressions. No options.
    "require-unicode-regexp": "error",

    # Require generator functions to contain `yield`. No options.
    "require-yield": "error",

    # Disallow space after spread operator. Default options.
    "rest-spread-spacing": "warn",

    # See @typescript-eslint/semi
    "semi": "off",

    # Enforce space after semicolons and disallow space before semicolons. Default options.
    "semi-spacing": "warn",

    # Enforce that semicolons are at the end of statements. Default options.
    "semi-style": "warn",

    # Enforce sorted import declarations within modules. Default options.
    "sort-imports": "warn",

    # Not useful.
    "sort-keys": "off",

    # Not useful.
    "sort-vars": "off",

    # See @typescript-eslint/space-before-blocks
    "space-before-blocks": "off",

    # See @typescript-eslint/space-before-function-paren
    "space-before-function-paren": "off",

    # Disallow spaces inside parentheses. Default options.
    "space-in-parens": "warn",

    # See @typescript-eslint/space-infix-ops
    "space-infix-ops": "off",

    # Enforce consistent spacing before or after unary operators. Default options.
    "space-unary-ops": "warn",

    # Enforce use of space at the beginning of comments. Default options.
    "spaced-comment": "warn",

    # Disallow strict mode directives.
    "strict": ["error", "never"],

    # Enforce space after colons and disallow space before colons in `switch`. Default options.
    "switch-colon-spacing": "warn",

    # Require `Symbol` descriptions. No options.
    "symbol-description": "warn",

    # Disallow spacing around embedded expressions of template strings. Default options.
    "template-curly-spacing": "warn",

    # Disallow spacing between a tag function and its template literal. Default options.
    "template-tag-spacing": "warn",

    # Disallow Unicode byte order mark (BOM). Default options.
    "unicode-bom": "error",

    # Disallow usual `===` comparisons when checking for `NaN`.
    "use-isnan": ["error", {"enforceForIndexOf": True}],

    # Enforce comparing `typeof` expressions against valid string literals.
    "valid-typeof": ["error", {"requireStringLiterals": True}],

    # Not needed because eslint/no-var disallows all usage of `var`.
    "vars-on-top": "off",

    # Require parentheses around the function expression in IIFE patterns.
    "wrap-iife": ["warn", "inside"],

    # Not useful.
    "wrap-regex": "off",

    # Enforce consistent spacing around the `*` in `yield*` expressions. Default options.
    "yield-star-spacing": "warn",

    # Disallow conditions where operands are in unusual order, e.g. `if (0 === x)`. Default options.
    "yoda": "warn",
}


svelte_rules = {
    # Disallow usage of <button> without an explicit type attribute. Default options.
    "button-has-type": "warn",

    # System: provides eslint-disable functionality in template HTML.
    "comment-directive": ["error", {"reportUnusedDisableDirectives": True}],

    # Enforce same variable names between values and callback in `derived`. No options.
    "derived-has-same-inputs-outputs": "warn",

    # Enforce consistent line breaks between HTML tag and first attribute. Default options.
    "first-attribute-linebreak": "warn",

    # Enforce consistent spacing in HTML tags. Default options.
    "html-closing-bracket-spacing": "warn",

    # Enforce consistent use of double quotes with HTML attributes.
    "html-quotes": ["warn", {
        "prefer": "double",
        "dynamic": {
            "quoted": False,
            "avoidInvalidUnquotedInHTML": True,
        },
    }],

    # Enforce consistent use of self-closing HTML tags. Default options.
    "html-self-closing": "warn",

    # Enforce consistent 4-space indentation. Overrides turn off eslint/indent.
    "indent": ["warn", {"indent": 4}],

    # Enforce the maximum number of attributes per line.
    "max-attributes-per-line": ["warn", {
        "multiline": 1,
        "singleline": 3,
    }],

    # Enforce no spacing inside mustache syntax. Default options.
    "mustache-spacing": "warn",

    # Disallow the use of `{@debug ...}`. No options.
    "no-at-debug-tags": "warn",

    # Disallow the use of `{@html ...}`. No options.
    "no-at-html-tags": "error",

    # Disallow manipulating the DOM. No options.
    "no-dom-manipulating": "error",

    # Disallow duplicate conditions in `{#if}` / `{:else if}` chains. No options.
    "no-dupe-else-if-blocks": "error",

    # Disallow duplicate `on:` directives. No options.
    "no-dupe-on-directives": "error",

    # Disallow duplicate `style` properties. No options.
    "no-dupe-style-properties": "error",

    # Disallow duplicate `use:` directives. No options.
    "no-dupe-use-directives": "error",

    # Disallow dynamic slot names. No options.
    "no-dynamic-slot-name": "error",

    # Disallow `load` function exports in *.svelte SvelteKit page components. No options.
    "no-export-load-in-svelte-module-in-kit-pages": "warn",

    # Disallow wrapping single reactive statements in curly braces. No options.
    "no-extra-reactive-curlies": "warn",

    # Disallow function and var declarations in nested blocks.
    # Overrides turn off eslint/no-inner-declarations.
    "no-inner-declarations": ["error", "both"],

    # Disallow use of non-functions as event handlers. No options.
    "no-not-function-handler": "error",

    # Disallow objects in text mustache interpolation. No options.
    "no-object-in-text-mustaches": "error",

    # Disallow assigning functions in reactive statements. No options.
    "no-reactive-functions": "warn",

    # Disallow assigning literals in reactive statements. No options.
    "no-reactive-literals": "warn",

    # Disallow shorthand style properties that override related longhand properties. No options.
    "no-shorthand-style-property-overrides": "error",

    # Disallow spaces around equal signs in attribute. No options.
    "no-spaces-around-equal-signs-in-attribute": "warn",

    # Disallow using async/await inside stores. No options.
    "no-store-async": "warn",

    # Disallow `target="_blank"` attribute without `rel="noopener noreferrer"`. Default options.
    "no-target-blank": "error",

    # Disallow trailing whitespace at the end of lines. Default options.
    # Overrides turn off eslint/no-trailing-spaces.
    "no-trailing-spaces": "error",

    # Disallow unknown CSS properties in `style:`. Default options.
    "no-unknown-style-directive-property": "warn",

    # Disallow unused `svelte-ignore` comments. No options.
    "no-unused-svelte-ignore": "warn",

    # Disallow unnecessary mustache interpolations with string literals. Default options.
    "no-useless-mustaches": "warn",

    # Require class directives instead of ternary expressions. No options.
    "prefer-class-directive": "warn",

    # Prefer destructuring values from object stores. No options.
    "prefer-destructured-store-props": "warn",

    # Require style directives instead of style attributes. No options.
    "prefer-style-directive": "warn",

    # Require style attributes that can be optimized. No options.
    "require-optimized-style-attribute": "warn",

    # Require that store callbacks use the `set` parameter. No options.
    "require-store-callbacks-use-set-param": "warn",

    # Disallow accessing stores without `.get()` or the `$` prefix. No options.
    "require-store-reactive-access": "warn",

    # Enforce setting initial values for stores. No options.
    "require-stores-init": "error",

    # Enforce use of shorthand syntax for attributes. Default options.
    "shorthand-attribute": "warn",

    # Enforce use of shorthand syntax for directives. Default options.
    "shorthand-directive": "warn",

    # Enforce consistent ordering of attributes. Default options.
    "sort-attributes": "warn",

    # Require spacing after `<!--` and before `-->` in HTML comments. Default options.
    "spaced-html-comment": "warn",

    # System: required for the svelte plugin to work.
    "system": "error",

    # Disallow warnings when compiling. Default options.
    "valid-compile": "warn",

    # Disallow props other than `data` or `errors` in SvelteKit page components. No options.
    "valid-prop-names-in-kit-pages": "error",
}


typescript_eslint_rules = {
    # Require that function overload signatures be consecutive. No options.
    "adjacent-overload-signatures": "warn",

    # Require using `T[]` for arrays of simple types and `Array<T>` for others.
    "array-type": ["warn", {"default": "array-simple"}],

    # Disallow awaiting a value that is not `Thenable`. No options.
    "await-thenable": "warn",

    # Disallow `@ts-<directive>` comments. Default options.
    "ban-ts-comment": "warn",

    # Disallow `// tslint:<rule-flag>` comments. No options.
    "ban-tslint-comment": "error",

    # Disallow using certain built-in types. Default options.
    "ban-types": "error",

    # Enforce "one true brace style". Default options. Extends eslint/brace-style.
    "brace-style": "warn",

    # Enforce consistent style for literals on classes. Default options.
    "class-literal-property-style": "error",

    # Enforce consistent use of trailing commas. Extends eslint/comma-dangle.
    "comma-dangle": ["warn", "always-multiline"],

    # Enforce consistent spacing around commas. Default options. Extends eslint/comma-spacing.
    "comma-spacing": "warn",

    # Enforce consistent style for using generic on constructor calls. Default options.
    "consistent-generic-constructors": "warn",

    # Enforce consistent use of `Record` over an `interface` only containing an index signature.
    # Default options.
    "consistent-indexed-object-style": "warn",

    # Disallow type assertions.
    "consistent-type-assertions": ["error", {"assertionStyle": "never"}],

    # Enforce consistent use of `interface` over `type`. Default options.
    "consistent-type-definitions": "warn",

    # Enforce consistent usage of `type` exports. Default options.
    "consistent-type-exports": "warn",

    # Enforce consistent usage of type imports. Default options.
    "consistent-type-imports": "warn",

    # Enforce default parameters to be last. No options. Extends eslint/default-param-last.
    "default-param-last": "error",

    # Enforce dot notation whenever possible. Default options. Extends eslint/dot-notation.
    "dot-notation": "warn",

    # Require explicit return types on functions and class methods.
    "explicit-function-return-type": ["warn", {
        "allowHigherOrderFunctions": False,
        "allowTypedFunctionExpressions": False,
    }],

    # Require explicit accessibility modifiers on class properties and methods. Default options.
    "explicit-member-accessibility": "warn",

    # Require explicit types on exported functions' and classes' public interfaces.
    "explicit-module-boundary-types": ["error", {
        "allowHigherOrderFunctions": False,
        "allowTypedFunctionExpressions": False,
    }],

    # Disallow spacing between function identifiers and their invocations.
    # Default options. Extends eslint/func-call-spacing.
    "func-call-spacing": "warn",

    # Enforce consistent 4-space indentation. Extends eslint/indent.
    "indent": ["warn", 4],

    # Not useful. Extends eslint/init-declarations.
    "init-declarations": "off",

    # Enforce consistent spacing around keywords. Default options. Extends eslint/keyword-spacing.
    "keyword-spacing": "warn",

    # Not useful. Extends eslint/lines-between-class-members.
    "lines-between-class-members": "off",

    # Require semicolons for delimiting members of interfaces and type literals.
    "member-delimiter-style": ["warn", {
        "singleline": {"requireLast": True},
    }],

    # Enforce a consistent member declaration order. Default options.
    "member-ordering": "warn",

    # Require property style for method signatures. Default options.
    "method-signature-style": "warn",

    # Enforce camelCase/PascalCase/UPPER_CASE naming. Default options.
    "naming-convention": "warn",

    # Disallow generic Array constructors. No options. Extends eslint/no-array-constructor.
    "no-array-constructor": "error",

    # Disallow `.toString()` when output is useless (e.g. "[object Object]"). Default options.
    "no-base-to-string": "error",

    # Disabled because @typescript-eslint/no-non-null-assertion disallows non-null assertions.
    "no-confusing-non-null-assertion": "off",

    # Require expressions of type `void` to appear in statement position. Default options.
    "no-confusing-void-expression": "error",

    # Disallow duplicate class members. No options. Extends eslint/no-dupe-class-members.
    "no-dupe-class-members": "error",

    # Disallow duplicate `enum` member values. No options.
    "no-duplicate-enum-values": "error",

    # Disallow using the delete operator on computed key expressions. No options.
    "no-dynamic-delete": "error",

    # Disallow empty functions. Default options. Extends eslint/no-empty-function.
    "no-empty-function": "warn",

    # Disallow the declaration of empty interfaces. Default options.
    "no-empty-interface": "warn",

    # Disallow the any type. Default options.
    "no-explicit-any": "error",

    # Disabled because @typescript-eslint/no-non-null-assertion disallows non-null assertions.
    "no-extra-non-null-assertion": "off",

    # Disallow unnecessary parentheses. Extends eslint/no-extra-parens.
    "no-extra-parens": ["warn", "all", {
        "conditionalAssign": True,
        "nestedBinaryExpressions": False,
        "returnAssign": True,
    }],

    # Disallow unnecessary semicolons. No options. Extends eslint/no-extra-semi.
    "no-extra-semi": "warn",

    # Disallow classes used as namespaces (static members only). Default options.
    "no-extraneous-class": "error",

    # Require `Promise`-like statements to be handled unless consumed with the `void` operator.
    # Default options.
    "no-floating-promises": "warn",

    # Disallow for-in loops. No options.
    "no-for-in-array": "error",

    # Disallow the use of `eval()`-like methods. No options. Extends eslint/no-implied-eval.
    "no-implied-eval": "error",

    # Disallow explicit type declarations when they can be inferred. Default options.
    "no-inferrable-types": "warn",

    # Disallow `this` keywords outside of classes or class-like objects.
    # Default options. Extends eslint/no-invalid-this.
    "no-invalid-this": "error",

    # Disallow void type outside of generic or return types. Default options.
    "no-invalid-void-type": "error",

    # Disallow function declarations that contain unsafe references inside loop statements.
    # No options. Extends eslint/no-loop-func.
    "no-loop-func": "warn",

    # Disallow number literals that lose precision. No options. Extends eslint/no-loss-of-precision.
    "no-loss-of-precision": "error",

    # Not useful. Extends eslint/no-magic-numbers.
    "no-magic-numbers": "off",

    # Disallow the void operator except when used to discard a value.
    "no-meaningless-void-operator": ["warn", {"checkNever": True}],

    # Enforce valid definition of new and constructor. No options.
    "no-misused-new": "error",

    # Disallow Promises in places not designed to handle them. Default options.
    "no-misused-promises": "error",

    # Disallow TypeScript namespaces. Default options.
    "no-namespace": "error",

    # Disabled because @typescript-eslint/no-non-null-assertion disallows non-null assertions.
    "no-non-null-asserted-nullish-coalescing": "off",

    # Disabled because @typescript-eslint/no-non-null-assertion disallows non-null assertions.
    "no-non-null-asserted-optional-chain": "off",

    # Disallow non-null assertions using the `!` postfix operator. No options.
    "no-non-null-assertion": "error",

    # Disallow redeclarations. Default options. Extends eslint/no-redeclare.
    "no-redeclare": "error",

    # Disallow members of unions and intersections that do nothing or override type information.
    # No options.
    "no-redundant-type-constituents": "error",

    # Disallow invocation of `require()`. No options.
    "no-require-imports": "error",

    # Not useful.
    "no-restricted-imports": "off",

    # Disallow shadowing names from outer scopes. Extends eslint/no-shadow.
    "no-shadow": ["warn", {
        "builtinGlobals": True,
        "ignoreTypeValueShadow": False
    }],

    # Disallow aliasing `this`. Default options.
    "no-this-alias": "error",

    # Disallow throwing literals as exceptions. Default options. Extends eslint/no-throw-literal.
    "no-throw-literal": "error",

    # Not useful.
    "no-type-alias": "off",

    # Disallow unnecessary equality comparisons against boolean literals. Default options.
    "no-unnecessary-boolean-literal-compare": "warn",

    # Disabled because this is a buggy mess.
    "no-unnecessary-condition": "off",

    # Disallow unnecessary qualifiers inside `enum`. No options.
    "no-unnecessary-qualifier": "warn",

    # Disallow type arguments that are equal to the default. No options.
    "no-unnecessary-type-arguments": "warn",

    # Disallow type assertions that do not change the type of an expression. Default options.
    "no-unnecessary-type-assertion": "warn",

    # Disallow unnecessary constraints on generic types. No options.
    "no-unnecessary-type-constraint": "warn",

    # Disallow calling a function with a value with type `any`. No options.
    "no-unsafe-argument": "error",

    # Disallow assigning a value with type `any` to variables and properties. No options.
    "no-unsafe-assignment": "error",

    # Disallow calling a value with type `any`. No options.
    "no-unsafe-call": "error",

    # Disallow unsafe declaration merging. No options.
    "no-unsafe-declaration-merging": "error",

    # Disallow member access on a value with type `any`. No options.
    "no-unsafe-member-access": "error",

    # Disallow returning a value with type `any` from a function. No options.
    "no-unsafe-return": "error",

    # Disallow unused expressions. Default options. Extends eslint/no-unused-expressions.
    "no-unused-expressions": "warn",

    # Disallow unused variables. Extends eslint/no-unused-vars.
    "no-unused-vars": ["warn", {"caughtErrors": "all"}],

    # Disallow the use of variables before they are defined. Extends eslint/no-use-before-define.
    "no-use-before-define": ["error", {"ignoreTypeReferences": False}],

    # Disallow unnecessary constructors. No options. Extends eslint/no-useless-constructor.
    "no-useless-constructor": "warn",

    # Disallow useless empty exports. No options.
    "no-useless-empty-export": "error",

    # Disabled because @typescript-eslint/no-require-imports disallows `require()`.
    "no-var-requires": "off",

    # Disabled because @typescript-eslint/no-non-null-assertion disallows non-null assertions.
    "non-nullable-type-assertion-style": "off",

    # Enforce spaces inside object literals, imports, etc. Extends eslint/object-curly-spacing.
    "object-curly-spacing": ["error", "always"],

    # Not useful.
    "padding-line-between-statements": "off",

    # Disallow parameter properties in class constructors. Default options.
    "parameter-properties": "error",

    # Enforce the use of `as const` over literal type. No options.
    "prefer-as-const": "warn",

    # Require each enum member value to be explicitly initialized. No options.
    "prefer-enum-initializers": "error",

    # Enforce the use of for-of loop over the standard for loop where possible. No options.
    "prefer-for-of": "warn",

    # Enforce using function types instead of interfaces with call signatures. No options.
    "prefer-function-type": "warn",

    # Enforce `includes` method over `indexOf` method. No options.
    "prefer-includes": "warn",

    # Require all enum members to be literal values. Default options.
    "prefer-literal-enum-member": "error",

    # Disabled because @typescript-eslint/no-namespace disallows namespaces.
    "prefer-namespace-keyword": "off",

    # Enforce using the nullish coalescing operator instead of logical chaining. Default options.
    "prefer-nullish-coalescing": "warn",

    # Enforce using concise optional chain expressions instead of chained logical ands,
    # negated logical ors, or empty objects. No options.
    "prefer-optional-chain": "warn",

    # Require private members to be marked as readonly if they're never modified
    # outside of the constructor. Default options.
    "prefer-readonly": "warn",

    # Require function parameters to be typed as `readonly`. Default options.
    "prefer-readonly-parameter-types": "warn",

    # Enforce using type parameter when calling `Array#reduce` instead of casting. No options.
    "prefer-reduce-type-parameter": "warn",

    # Enforce `RegExp#exec` over `String#match` if no global flag is provided. No options.
    "prefer-regexp-exec": "warn",

    # Enforce that `this` is used when only `this` type is returned. No options.
    "prefer-return-this-type": "error",

    # Prefer using `String#startsWith` and `String#endsWith` over handling substrings. No options.
    "prefer-string-starts-ends-with": "warn",

    # Disabled because @typescript-eslint/ban-ts-comment disallows `@ts-<directive>` comments.
    "prefer-ts-expect-error": "off",

    # Not useful.
    "promise-function-async": "off",

    # Prefer the use of double quotes. Default options. Extends eslint/quotes.
    "quotes": "warn",

    # Require `Array#sort´ calls with non-string arrays to always provide a `compareFunction`.
    "require-array-sort-compare": ["error", {
        "ignoreStringArrays": True,
    }],

    # Disallow async functions without an `await` expression.
    # No options. Extends eslint/require-await.
    "require-await": "error",

    # Require both operands of addition to be the same type and be bigint, number, or string.
    "restrict-plus-operands": ["error", {
        "checkCompoundAssignments": True,
    }],

    # Disallow types from template literals if their `.toString()` output is useless
    # (mostly everything except strings and numbers). Default options.
    "restrict-template-expressions": "warn",

    # Disallow unnecessary `return await`. No options. Extends eslint/no-return-await.
    "return-await": "error",

    # Require semicolons at the end of statements. Default options. Extends eslint/semi.
    "semi": "warn",

    # Not useful.
    "sort-type-constituents": "off",

    # Require space before blocks. Default options. Extends eslint/space-before-blocks.
    "space-before-blocks": "warn",

    # Enforce consistent spacing in function definition. Extends eslint/space-before-function-paren.
    "space-before-function-paren": ["warn", {
        "anonymous": "never",
        "named": "never"
    }],

    # Require spacing around infix operators. Default options. Extends eslint/space-infix-ops.
    "space-infix-ops": "warn",

    # Disallow certain types, mostly nullable, in boolean expressions. Default options.
    "strict-boolean-expressions": "error",

    # Require `switch` statements to be exhaustive with union type. No options.
    "switch-exhaustiveness-check": "error",

    # Disallow certain triple slash directives in favor of ES6-style import declarations.
    "triple-slash-reference": ["error", {
        "lib": "never",
        "path": "never",
        "types": "never",
    }],

    # Require consistent spacing around type annotations. Default options.
    "type-annotation-spacing": "warn",

    # Not useful.
    "typedef": "off",

    # Enforce unbound methods are called with their expected scope. Default options.
    "unbound-method": "error",

    # Disallow overloads that could be unified with a union or optional/rest parameters.
    # Default options.
    "unified-signatures": "error",
}


# from_js* lists come directly from the npm packages; fill these from get_eslint_rules.js etc.
rule_sources = {
    "eslint": {
        "prefix": "",
        "rules": eslint_rules,
        "updated": "2023-01-06",
        "version": "8.31.0",
        "from_js": ["accessor-pairs", "array-bracket-newline", "array-bracket-spacing", "array-callback-return", "array-element-newline", "arrow-body-style", "arrow-parens", "arrow-spacing", "block-scoped-var", "block-spacing", "brace-style", "camelcase", "capitalized-comments", "class-methods-use-this", "comma-dangle", "comma-spacing", "comma-style", "complexity", "computed-property-spacing", "consistent-return", "consistent-this", "constructor-super", "curly", "default-case", "default-case-last", "default-param-last", "dot-location", "dot-notation", "eol-last", "eqeqeq", "for-direction", "func-call-spacing", "func-name-matching", "func-names", "func-style", "function-call-argument-newline", "function-paren-newline", "generator-star-spacing", "getter-return", "grouped-accessor-pairs", "guard-for-in", "id-denylist", "id-length", "id-match", "implicit-arrow-linebreak", "indent", "init-declarations", "jsx-quotes", "key-spacing", "keyword-spacing", "line-comment-position", "linebreak-style", "lines-around-comment", "lines-between-class-members", "logical-assignment-operators", "max-classes-per-file", "max-depth", "max-len", "max-lines", "max-lines-per-function", "max-nested-callbacks", "max-params", "max-statements", "max-statements-per-line", "multiline-comment-style", "multiline-ternary", "new-cap", "new-parens", "newline-per-chained-call", "no-alert", "no-array-constructor", "no-async-promise-executor", "no-await-in-loop", "no-bitwise", "no-caller", "no-case-declarations", "no-class-assign", "no-compare-neg-zero", "no-cond-assign", "no-confusing-arrow", "no-console", "no-const-assign", "no-constant-binary-expression", "no-constant-condition", "no-constructor-return", "no-continue", "no-control-regex", "no-debugger", "no-delete-var", "no-div-regex", "no-dupe-args", "no-dupe-class-members", "no-dupe-else-if", "no-dupe-keys", "no-duplicate-case", "no-duplicate-imports", "no-else-return", "no-empty", "no-empty-character-class", "no-empty-function", "no-empty-pattern", "no-empty-static-block", "no-eq-null", "no-eval", "no-ex-assign", "no-extend-native", "no-extra-bind", "no-extra-boolean-cast", "no-extra-label", "no-extra-parens", "no-extra-semi", "no-fallthrough", "no-floating-decimal", "no-func-assign", "no-global-assign", "no-implicit-coercion", "no-implicit-globals", "no-implied-eval", "no-import-assign", "no-inline-comments", "no-inner-declarations", "no-invalid-regexp", "no-invalid-this", "no-irregular-whitespace", "no-iterator", "no-label-var", "no-labels", "no-lone-blocks", "no-lonely-if", "no-loop-func", "no-loss-of-precision", "no-magic-numbers", "no-misleading-character-class", "no-mixed-operators", "no-mixed-spaces-and-tabs", "no-multi-assign", "no-multi-spaces", "no-multi-str", "no-multiple-empty-lines", "no-negated-condition", "no-nested-ternary", "no-new", "no-new-func", "no-new-native-nonconstructor", "no-new-object", "no-new-symbol", "no-new-wrappers", "no-nonoctal-decimal-escape", "no-obj-calls", "no-octal", "no-octal-escape", "no-param-reassign", "no-plusplus", "no-promise-executor-return", "no-proto", "no-prototype-builtins", "no-redeclare", "no-regex-spaces", "no-restricted-exports", "no-restricted-globals", "no-restricted-imports", "no-restricted-properties", "no-restricted-syntax", "no-return-assign", "no-return-await", "no-script-url", "no-self-assign", "no-self-compare", "no-sequences", "no-setter-return", "no-shadow", "no-shadow-restricted-names", "no-sparse-arrays", "no-tabs", "no-template-curly-in-string", "no-ternary", "no-this-before-super", "no-throw-literal", "no-trailing-spaces", "no-undef", "no-undef-init", "no-undefined", "no-underscore-dangle", "no-unexpected-multiline", "no-unmodified-loop-condition", "no-unneeded-ternary", "no-unreachable", "no-unreachable-loop", "no-unsafe-finally", "no-unsafe-negation", "no-unsafe-optional-chaining", "no-unused-expressions", "no-unused-labels", "no-unused-private-class-members", "no-unused-vars", "no-use-before-define", "no-useless-backreference", "no-useless-call", "no-useless-catch", "no-useless-computed-key", "no-useless-concat", "no-useless-constructor", "no-useless-escape", "no-useless-rename", "no-useless-return", "no-var", "no-void", "no-warning-comments", "no-whitespace-before-property", "no-with", "nonblock-statement-body-position", "object-curly-newline", "object-curly-spacing", "object-property-newline", "object-shorthand", "one-var", "one-var-declaration-per-line", "operator-assignment", "operator-linebreak", "padded-blocks", "padding-line-between-statements", "prefer-arrow-callback", "prefer-const", "prefer-destructuring", "prefer-exponentiation-operator", "prefer-named-capture-group", "prefer-numeric-literals", "prefer-object-has-own", "prefer-object-spread", "prefer-promise-reject-errors", "prefer-regex-literals", "prefer-rest-params", "prefer-spread", "prefer-template", "quote-props", "quotes", "radix", "require-atomic-updates", "require-await", "require-unicode-regexp", "require-yield", "rest-spread-spacing", "semi", "semi-spacing", "semi-style", "sort-imports", "sort-keys", "sort-vars", "space-before-blocks", "space-before-function-paren", "space-in-parens", "space-infix-ops", "space-unary-ops", "spaced-comment", "strict", "switch-colon-spacing", "symbol-description", "template-curly-spacing", "template-tag-spacing", "unicode-bom", "use-isnan", "valid-typeof", "vars-on-top", "wrap-iife", "wrap-regex", "yield-star-spacing", "yoda"],
        "from_js_deprecated": ["callback-return", "global-require", "handle-callback-err", "id-blacklist", "indent-legacy", "lines-around-directive", "newline-after-var", "newline-before-return", "no-buffer-constructor", "no-catch-shadow", "no-mixed-requires", "no-native-reassign", "no-negated-in-lhs", "no-new-require", "no-path-concat", "no-process-env", "no-process-exit", "no-restricted-modules", "no-spaced-func", "no-sync", "prefer-reflect", "require-jsdoc", "valid-jsdoc"],
    },
    "svelte": {
        "prefix": "svelte",
        "rules": svelte_rules,
        "updated": "2023-01-08",
        "version": "2.14.1",
        "from_js": ["button-has-type", "comment-directive", "derived-has-same-inputs-outputs", "first-attribute-linebreak", "html-closing-bracket-spacing", "html-quotes", "html-self-closing", "indent", "max-attributes-per-line", "mustache-spacing", "no-at-debug-tags", "no-at-html-tags", "no-dom-manipulating", "no-dupe-else-if-blocks", "no-dupe-on-directives", "no-dupe-style-properties", "no-dupe-use-directives", "no-dynamic-slot-name", "no-export-load-in-svelte-module-in-kit-pages", "no-extra-reactive-curlies", "no-inner-declarations", "no-not-function-handler", "no-object-in-text-mustaches", "no-reactive-functions", "no-reactive-literals", "no-shorthand-style-property-overrides", "no-spaces-around-equal-signs-in-attribute", "no-store-async", "no-target-blank", "no-trailing-spaces", "no-unknown-style-directive-property", "no-unused-svelte-ignore", "no-useless-mustaches", "prefer-class-directive", "prefer-destructured-store-props", "prefer-style-directive", "require-optimized-style-attribute", "require-store-callbacks-use-set-param", "require-store-reactive-access", "require-stores-init", "shorthand-attribute", "shorthand-directive", "sort-attributes", "spaced-html-comment", "system", "valid-compile", "valid-prop-names-in-kit-pages"], 
        "from_js_deprecated": ["@typescript-eslint/no-unnecessary-condition"],
    },
    "typescript-eslint": {
        "prefix": "@typescript-eslint",
        "rules": typescript_eslint_rules,
        "updated": "2023-01-06",
        "version": "5.48.0",
        "from_js": ["adjacent-overload-signatures", "array-type", "await-thenable", "ban-ts-comment", "ban-tslint-comment", "ban-types", "brace-style", "class-literal-property-style", "comma-dangle", "comma-spacing", "consistent-generic-constructors", "consistent-indexed-object-style", "consistent-type-assertions", "consistent-type-definitions", "consistent-type-exports", "consistent-type-imports", "default-param-last", "dot-notation", "explicit-function-return-type", "explicit-member-accessibility", "explicit-module-boundary-types", "func-call-spacing", "indent", "init-declarations", "keyword-spacing", "lines-between-class-members", "member-delimiter-style", "member-ordering", "method-signature-style", "naming-convention", "no-array-constructor", "no-base-to-string", "no-confusing-non-null-assertion", "no-confusing-void-expression", "no-dupe-class-members", "no-duplicate-enum-values", "no-dynamic-delete", "no-empty-function", "no-empty-interface", "no-explicit-any", "no-extra-non-null-assertion", "no-extra-parens", "no-extra-semi", "no-extraneous-class", "no-floating-promises", "no-for-in-array", "no-implied-eval", "no-inferrable-types", "no-invalid-this", "no-invalid-void-type", "no-loop-func", "no-loss-of-precision", "no-magic-numbers", "no-meaningless-void-operator", "no-misused-new", "no-misused-promises", "no-namespace", "no-non-null-asserted-nullish-coalescing", "no-non-null-asserted-optional-chain", "no-non-null-assertion", "no-redeclare", "no-redundant-type-constituents", "no-require-imports", "no-restricted-imports", "no-shadow", "no-this-alias", "no-throw-literal", "no-type-alias", "no-unnecessary-boolean-literal-compare", "no-unnecessary-condition", "no-unnecessary-qualifier", "no-unnecessary-type-arguments", "no-unnecessary-type-assertion", "no-unnecessary-type-constraint", "no-unsafe-argument", "no-unsafe-assignment", "no-unsafe-call", "no-unsafe-declaration-merging", "no-unsafe-member-access", "no-unsafe-return", "no-unused-expressions", "no-unused-vars", "no-use-before-define", "no-useless-constructor", "no-useless-empty-export", "no-var-requires", "non-nullable-type-assertion-style", "object-curly-spacing", "padding-line-between-statements", "parameter-properties", "prefer-as-const", "prefer-enum-initializers", "prefer-for-of", "prefer-function-type", "prefer-includes", "prefer-literal-enum-member", "prefer-namespace-keyword", "prefer-nullish-coalescing", "prefer-optional-chain", "prefer-readonly", "prefer-readonly-parameter-types", "prefer-reduce-type-parameter", "prefer-regexp-exec", "prefer-return-this-type", "prefer-string-starts-ends-with", "prefer-ts-expect-error", "promise-function-async", "quotes", "require-array-sort-compare", "require-await", "restrict-plus-operands", "restrict-template-expressions", "return-await", "semi", "sort-type-constituents", "space-before-blocks", "space-before-function-paren", "space-infix-ops", "strict-boolean-expressions", "switch-exhaustiveness-check", "triple-slash-reference", "type-annotation-spacing", "typedef", "unbound-method", "unified-signatures"],
        "from_js_deprecated": ["no-duplicate-imports", "no-implicit-any-catch", "no-parameter-properties", "sort-type-union-intersection-members"],
    },
}


def prefix_name(name, prefix):
    if not prefix:
        return name
    return f"{prefix}/{name}"


def prefix_rules(rule_dict, prefix):
    return {
        prefix_name(name, prefix): value for name, value in rule_dict.items()
    }


def get_rules_prefixed(source_names):
    rules = {}
    for source_name in source_names:
        source = rule_sources[source_name]
        rules |= {
            prefix_name(name, source["prefix"]): value
            for name, value in source["rules"].items()
        }
    return rules


def run_checks():
    errors = False
    error_messages = ["Some errors were found:"]

    # Initialize with all rules, assert to be empty after loops
    extraneous_rules = set(get_rules_prefixed(rule_sources))

    missing_rules = set()
    duplicate_rules_in_from_js = set()

    for source_name, source in rule_sources.items():
        # Check that rules are sorted.
        if list(source["rules"]) != sorted(source["rules"]):
            errors = True
            error_messages.append(f"- Rules in '{source_name}' are not sorted correctly")

        # Check that all rules are specified.
        for rule_name in source["from_js"]:
            rule_name_prefixed = prefix_name(rule_name, source["prefix"])
            try:
                extraneous_rules.remove(rule_name_prefixed)
            except KeyError:
                if rule_name not in source["rules"]:
                    missing_rules.add(rule_name_prefixed)
                else:
                    duplicate_rules_in_from_js.add(rule_name_prefixed)

    if missing_rules:
        errors = True
        missing_rules_list = "\n".join(f"  - {rule}" for rule in missing_rules)
        error_messages.append(f"- Some rules are missing:\n{missing_rules_list}")

    if duplicate_rules_in_from_js:
        errors = True
        duplicate_rules_list = "\n".join(f"  - {rule}" for rule in duplicate_rules_in_from_js)
        error_messages.append(f"- Some rules are duplicated in `from_js`:\n{duplicate_rules_list}")

    if extraneous_rules:
        errors = True

        all_deprecated_rules_prefixed = set()
        for source in rule_sources.values():
            all_deprecated_rules_prefixed |= {
                prefix_name(name, source["prefix"]) for name in source["from_js_deprecated"]
            }

        deprecated_rules = set()
        other_extraneous_rules = set()
        for rule_name in extraneous_rules:
            if rule_name in all_deprecated_rules_prefixed:
                deprecated_rules.add(rule_name)
            else:
                other_extraneous_rules.add(rule_name)

        if deprecated_rules:
            deprecated_rules_list = "\n".join(f" - {rule}" for rule in deprecated_rules)
            error_messages.append(f"- Some deprecated rules were used:\n{deprecated_rules_list}")

        if other_extraneous_rules:
            extraneous_rules_list = "\n".join(f"  - {rule}" for rule in other_extraneous_rules)
            error_messages.append(f"- Some rules were not found in any sources:\n{extraneous_rules_list}")

    if errors:
        print("\n\n".join(error_messages), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    configs = {
        "svelte": {
            "rule_sources": ["eslint", "svelte", "typescript-eslint"],
            "eslint_base": {
                "overrides": [
                    {
                        "files": ["*.svelte"],
                        "parser": "svelte-eslint-parser",
                        "parserOptions": {"parser": "@typescript-eslint/parser"},
                        "rules": {
                            "no-inner-declarations": "off",
                            "no-trailing-spaces": "off",
                            "@typescript-eslint/indent": "off",
                        },
                    },
                ],
                "parser": "@typescript-eslint/parser",
                "parserOptions": {
                    "extraFileExtensions": [".svelte"],
                    "project": "tsconfig.json",
                },
                "root": True,
            },
        },
        "typescript-node": {
            "rule_sources": ["eslint", "typescript-eslint"],
            "eslint_base": {
                "env": {"node": True},
                "overrides": [
                    {"files": ["*.ts"]},
                ],
                "parser": "@typescript-eslint/parser",
                "parserOptions": {
                    "project": "tsconfig.json",
                },
                "plugins": ["@typescript-eslint"],
                "root": True,
            },
        },
    }

    try:
        config = configs[sys.argv[1]]
    except (IndexError, KeyError):
        config_names = " | ".join(configs)
        print(f"Usage: {sys.argv[0]} {{ {config_names} }}", file=sys.stderr)
        sys.exit(1)

    run_checks()

    print(
        json.dumps(
            config["eslint_base"] | {"rules": get_rules_prefixed(config["rule_sources"])},
            indent=4
        )
    )
