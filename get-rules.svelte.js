#!/usr/bin/env node

const ruleData = require("eslint-plugin-svelte").rules;

const rules = [];
const rulesDeprecated = [];

for (const [name, data] of Object.entries(ruleData)) {
    const list = data.meta.deprecated ? rulesDeprecated : rules;
    list.push(name);
}

const listify = rules => `[${rules.map(rule => `"${rule}"`).join(", ")}]`
console.log(`\
"from_js": ${listify(rules)}

"from_js_deprecated": ${listify(rulesDeprecated)}\
`);
