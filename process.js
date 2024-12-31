- function processData(data) {
-     return data.map(item => item.value);
- }
+ function processData(data) {
+     if (!Array.isArray(data) || data.length === 0) {
+         throw new Error('Invalid input: data must be a non-empty array.');
+     }
+     return data.map(item => item.value);
+ }
