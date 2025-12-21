# Test Log Report: maryangel101_robustness_mode-examples_seed1.jsonl

- total: 10
- correct: 9
- no_match: 1
- accuracy: 0.9000

### #1 | OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- confidence: 1.0
- true_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- matched_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-each/node_modules/@sinclair/typebox/typebox.d.ts: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest-each/node_modules/@sinclair/typebox/typebox.d.ts’: No such file or directory
```

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`

### #2 | OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- confidence: 1.0
- true_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- matched_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-each/node_modules/@sinclair/typebox/typebox.d.ts: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest-each/node_modules/@sinclair/typebox/typebox.d.ts’: No such file or directory
```

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`

### #3 | OK

- true_cluster_id: 127
- predicted_cluster_id: 127
- confidence: 1.0
- true_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- matched_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@jest/types/node_modules/@sinclair/typebox/system: Cannot mkdir: No such file or directory
```

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest: Cannot mkdir: No such file or directory`

### #4 | OK

- true_cluster_id: 127
- predicted_cluster_id: 127
- confidence: 1.0
- true_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- matched_template: `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**base_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@jest/types/node_modules/@sinclair/typebox/system: Cannot mkdir: No such file or directory
```

**mutated_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules_v2/@jest/types/node_modules/@sinclair/typebox/system: Cannot mkdir: No such file or directory
```

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest: Cannot mkdir: No such file or directory`

### #5 | OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- confidence: 1.0
- true_template: `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- matched_template: `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`

**log**
```
Received 377487360 of 1274821257 (29.6%), 90.0 MBs/sec
```

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`

### #6 | OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- confidence: 1.0
- true_template: `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- matched_template: `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`

**log**
```
Received 377487360 of 1274821257 (29.6%), 90.0 MBs/sec
```

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`

### #7 | WRONG

- true_cluster_id: 144
- predicted_cluster_id: -1
- confidence: 0.0
- true_template: `Done in 0.79s.`
- matched_template: `No match`

**base_log**
```
Done in 3.88s.
```

**mutated_log**
```
Error: Done in 3.88s.
```

### #8 | OK

- true_cluster_id: 144
- predicted_cluster_id: 144
- confidence: 1.0
- true_template: `Done in 0.79s.`
- matched_template: `Done in 0.79s.`

**log**
```
Done in 3.88s.
```

**predicted_cluster_examples (head)**
- `Done in 0.79s.`
- `Done in 0.53s.`

### #9 | OK

- true_cluster_id: 143
- predicted_cluster_id: 143
- confidence: 1.0
- true_template: `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- matched_template: `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`

**log**
```
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig
```

**predicted_cluster_examples (head)**
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node/.flowconfig`

### #10 | OK

- true_cluster_id: 143
- predicted_cluster_id: 143
- confidence: 1.0
- true_template: `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- matched_template: `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`

**base_log**
```
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig
```

**mutated_log**
```
Wrote a Flow config to /home/runner/work/react/react/scripts/flow-new/dom-browser/.flowconfig
```

**predicted_cluster_examples (head)**
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node/.flowconfig`
