# dec2vec Robustness Report: maryangel101_dec2vec_robustness_seed0.jsonl

- total: 60
- hit@1: 39 (0.6500)
- hit@k: 49 (0.8167)

## #1 | TOP1_OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- topk: 5

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js’: No such file or directory
```

**top_matches**
- score=0.9951 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9804 tag=121 cid=121 tmpl=`key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9777 tag=132 cid=132 tmpl=`Cache not found for input keys: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d35...`
- score=0.9739 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9739 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #2 | TOP1_OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- topk: 5

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js’: No such file or directory
```

**top_matches**
- score=0.9951 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9804 tag=121 cid=121 tmpl=`key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9777 tag=132 cid=132 tmpl=`Cache not found for input keys: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d35...`
- score=0.9739 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9739 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #3 | TOPK_OK

- true_cluster_id: 127
- predicted_cluster_id: 128
- topk: 5

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/traverse/node_modules: Cannot mkdir: No such file or directory
```

**top_matches**
- score=0.9879 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9843 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9843 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9774 tag=68 cid=68 tmpl=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.9673 tag=126 cid=126 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler: Cannot mkdir: File exists`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #4 | TOPK_OK

- true_cluster_id: 127
- predicted_cluster_id: 128
- topk: 5

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/traverse/node_modules: Cannot mkdir: No such file or directory
```

**top_matches**
- score=0.9879 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9843 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9843 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9774 tag=68 cid=68 tmpl=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.9673 tag=126 cid=126 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler: Cannot mkdir: File exists`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #5 | TOP1_OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- topk: 5

**base_log**
```
Received 134217728 of 1274692111 (10.5%), 119.6 MBs/sec
```

**mutated_log**
```
Error: Received 134217728 of 1274692111 (10.5%), 242.6 MBs/sec
```

**top_matches**
- score=0.9913 tag=115 cid=115 tmpl=`Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- score=0.9896 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9878 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9877 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`
- score=0.9861 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`
- `Received 264241152 of 1274821257 (20.7%), 84.0 MBs/sec`

## #6 | TOP1_OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- topk: 5

**base_log**
```
Received 134217728 of 1274692111 (10.5%), 119.6 MBs/sec
```

**mutated_log**
```
Error: Received 134217728 of 1274692111 (10.5%), 119.6 MBs/sec
```

**top_matches**
- score=0.9913 tag=115 cid=115 tmpl=`Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- score=0.9896 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9878 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9877 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`
- score=0.9861 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`
- `Received 264241152 of 1274821257 (20.7%), 84.0 MBs/sec`

## #7 | TOP1_OK

- true_cluster_id: 144
- predicted_cluster_id: 144
- topk: 5

**base_log**
```
Done in 0.56s.
```

**mutated_log**
```
Done in 0.11s.
```

**top_matches**
- score=1.0000 tag=144 cid=144 tmpl=`Done in 0.79s.`
- score=0.6592 tag=28 cid=28 tmpl=`token: ***`
- score=0.4985 tag=182 cid=182 tmpl=`Post job cleanup.`
- score=0.4391 tag=16 cid=16 tmpl=`##[group]GITHUB_TOKEN Permissions`
- score=0.4204 tag=21 cid=21 tmpl=`Getting action download info`

**predicted_cluster_examples (head)**
- `Done in 0.79s.`
- `Done in 0.53s.`
- `Done in 1.53s.`

## #8 | TOP1_OK

- true_cluster_id: 144
- predicted_cluster_id: 144
- topk: 5

**log**
```
Done in 0.56s.
```

**top_matches**
- score=1.0000 tag=144 cid=144 tmpl=`Done in 0.79s.`
- score=0.6592 tag=28 cid=28 tmpl=`token: ***`
- score=0.4985 tag=182 cid=182 tmpl=`Post job cleanup.`
- score=0.4391 tag=16 cid=16 tmpl=`##[group]GITHUB_TOKEN Permissions`
- score=0.4204 tag=21 cid=21 tmpl=`Getting action download info`

**predicted_cluster_examples (head)**
- `Done in 0.79s.`
- `Done in 0.53s.`
- `Done in 1.53s.`

## #9 | TOP1_OK

- true_cluster_id: 143
- predicted_cluster_id: 143
- topk: 5

**log**
```
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/fabric/.flowconfig
```

**top_matches**
- score=0.9994 tag=143 cid=143 tmpl=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- score=0.9848 tag=220 cid=220 tmpl=`'react-hooks/set-state-in-render': 'error',`
- score=0.9828 tag=217 cid=217 tmpl=`'react-hooks/set-state-in-effect': 'error',`
- score=0.9819 tag=218 cid=218 tmpl=`'react-hooks/error-boundaries': 'error',`
- score=0.9808 tag=214 cid=214 tmpl=`'react-hooks/immutability': 'error',`

**predicted_cluster_examples (head)**
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node-webpack/.flowconfig`

## #10 | TOP1_OK

- true_cluster_id: 143
- predicted_cluster_id: 143
- topk: 5

**log**
```
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/fabric/.flowconfig
```

**top_matches**
- score=0.9994 tag=143 cid=143 tmpl=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- score=0.9848 tag=220 cid=220 tmpl=`'react-hooks/set-state-in-render': 'error',`
- score=0.9828 tag=217 cid=217 tmpl=`'react-hooks/set-state-in-effect': 'error',`
- score=0.9819 tag=218 cid=218 tmpl=`'react-hooks/error-boundaries': 'error',`
- score=0.9808 tag=214 cid=214 tmpl=`'react-hooks/immutability': 'error',`

**predicted_cluster_examples (head)**
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node/.flowconfig`
- `Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-node-webpack/.flowconfig`

## #11 | TOP1_OK

- true_cluster_id: 47
- predicted_cluster_id: 47
- topk: 5

**base_log**
```
Temporarily overriding HOME='/home/runner/work/_temp/654ab7c7-62ca-4427-97bf-c7be3561699d' before making global git config changes
```

**mutated_log**
```
Temporarily overriding HOME='/home/runner/work/_temp/8102c0fa-7a26-774e-22af-3993a69e2ca7' before making global git config changes
```

**top_matches**
- score=0.9707 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9534 tag=61 cid=61 tmpl=`hint: Disable this message with "git config set advice.defaultBranchName false"`
- score=0.9531 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9525 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`
- score=0.9490 tag=53 cid=53 tmpl=`hint: Using 'master' as the name for the initial branch. This default branch name`

**predicted_cluster_examples (head)**
- `Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/0f5c664f-5b52-45ed-9fa6-dd937c2019ed' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`

## #12 | TOP1_OK

- true_cluster_id: 47
- predicted_cluster_id: 47
- topk: 5

**base_log**
```
Temporarily overriding HOME='/home/runner/work/_temp/654ab7c7-62ca-4427-97bf-c7be3561699d' before making global git config changes
```

**mutated_log**
```
Temporarily overriding HOME='/home/runner/work/_temp/654ab7c7-20ca-4427-97bf-c7be3561699d' before making global git config changes
```

**top_matches**
- score=0.9683 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9666 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9641 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9635 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9513 tag=71 cid=71 tmpl=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`

**predicted_cluster_examples (head)**
- `Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/0f5c664f-5b52-45ed-9fa6-dd937c2019ed' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`

## #13 | TOP1_OK

- true_cluster_id: 117
- predicted_cluster_id: 117
- topk: 5

**base_log**
```
[command]/usr/bin/tar -xf /home/runner/work/_temp/58534da2-72ae-4eb6-9045-c5349e2dab20/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**mutated_log**
```
[command]/usr/bin/tar -xf /home/runner/work/_temp/24412c87-6d8e-fb2a-3fa6-70837b5ad134/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**top_matches**
- score=0.9964 tag=117 cid=117 tmpl=`[command]/usr/bin/tar -xf /home/runner/work/_temp/6fe4625a-4086-40e6-a910-3e916ffb47fa/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9938 tag=198 cid=198 tmpl=`[command]/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/react/react --files-from manifest.txt --use-compre...`
- score=0.9858 tag=49 cid=49 tmpl=`[command]/usr/bin/git config --global --add safe.directory /home/runner/work/react/react`
- score=0.9729 tag=126 cid=126 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler: Cannot mkdir: File exists`
- score=0.9720 tag=52 cid=52 tmpl=`[command]/usr/bin/git init /home/runner/work/react/react`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/6fe4625a-4086-40e6-a910-3e916ffb47fa/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/f7f85e1c-6683-45b8-b1f4-3b683d246791/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/da668ef2-09dd-4b0f-ab03-20889d1c5c95/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`

## #14 | TOPK_OK

- true_cluster_id: 117
- predicted_cluster_id: 198
- topk: 5

**log**
```
[command]/usr/bin/tar -xf /home/runner/work/_temp/58534da2-72ae-4eb6-9045-c5349e2dab20/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**top_matches**
- score=0.9995 tag=198 cid=198 tmpl=`[command]/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/react/react --files-from manifest.txt --use-compre...`
- score=0.9995 tag=117 cid=117 tmpl=`[command]/usr/bin/tar -xf /home/runner/work/_temp/6fe4625a-4086-40e6-a910-3e916ffb47fa/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9820 tag=52 cid=52 tmpl=`[command]/usr/bin/git init /home/runner/work/react/react`
- score=0.9785 tag=49 cid=49 tmpl=`[command]/usr/bin/git config --global --add safe.directory /home/runner/work/react/react`
- score=0.9694 tag=63 cid=63 tmpl=`[command]/usr/bin/git remote add origin https://github.com/facebook/react`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/react/react --files-from manifest.txt --use-compress-program zstdmt`

## #15 | TOP1_OK

- true_cluster_id: 102
- predicted_cluster_id: 102
- topk: 5

**log**
```
[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/68d379ce-4198-47ac-b596-b8c0c46bcde9 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52
```

**top_matches**
- score=0.9953 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9534 tag=60 cid=60 tmpl=`hint: git branch -m <name>`
- score=0.9392 tag=71 cid=71 tmpl=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`
- score=0.9334 tag=84 cid=84 tmpl=`git switch -c <new-branch-name>`
- score=0.9320 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc -f /home/runner/work/_temp/1a1c40e2-9dbf-49f3-ac81-2bbf2d87c2a4`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/68d379ce-4198-47ac-b596-b8c0c46bcde9 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/27b98926-9f2d-42d4-ab15-25d4938652d6 -f /home/runner/work/_temp/446bb931-0937-4eec-8e1e-a072e8c51220`

## #16 | TOP1_OK

- true_cluster_id: 102
- predicted_cluster_id: 102
- topk: 5

**base_log**
```
[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/68d379ce-4198-47ac-b596-b8c0c46bcde9 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52
```

**mutated_log**
```
[command]/usr/bin/tar_v2 xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/b310653f-610d-3827-29bd-51e13c68bf56 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52
```

**top_matches**
- score=0.9943 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9551 tag=60 cid=60 tmpl=`hint: git branch -m <name>`
- score=0.9389 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9389 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- score=0.9357 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc -f /home/runner/work/_temp/1a1c40e2-9dbf-49f3-ac81-2bbf2d87c2a4`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/68d379ce-4198-47ac-b596-b8c0c46bcde9 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/27b98926-9f2d-42d4-ab15-25d4938652d6 -f /home/runner/work/_temp/446bb931-0937-4eec-8e1e-a072e8c51220`

## #17 | TOP1_OK

- true_cluster_id: 23
- predicted_cluster_id: 23
- topk: 5

**base_log**
```
Complete job name: ESLint v7
```

**mutated_log**
```
Error: Complete job name: ESLint v7
```

**top_matches**
- score=0.9773 tag=23 cid=23 tmpl=`Complete job name: ESLint v7`
- score=0.9765 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9753 tag=61 cid=61 tmpl=`hint: Disable this message with "git config set advice.defaultBranchName false"`
- score=0.9569 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9473 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`

**predicted_cluster_examples (head)**
- `Complete job name: ESLint v7`
- `Complete job name: ESLint v8`
- `Complete job name: ESLint v6`

## #18 | TOP1_OK

- true_cluster_id: 23
- predicted_cluster_id: 23
- topk: 5

**log**
```
Complete job name: ESLint v7
```

**top_matches**
- score=1.0000 tag=23 cid=23 tmpl=`Complete job name: ESLint v7`
- score=0.9750 tag=61 cid=61 tmpl=`hint: Disable this message with "git config set advice.defaultBranchName false"`
- score=0.9585 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9575 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9555 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`

**predicted_cluster_examples (head)**
- `Complete job name: ESLint v7`
- `Complete job name: ESLint v8`
- `Complete job name: ESLint v6`

## #19 | TOP1_OK

- true_cluster_id: 116
- predicted_cluster_id: 116
- topk: 5

**log**
```
Cache Size: ~1216 MB (1274821257 B)
```

**top_matches**
- score=1.0000 tag=116 cid=116 tmpl=`Cache Size: ~1216 MB (1274821257 B)`
- score=0.9708 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9490 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`
- score=0.9474 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9450 tag=92 cid=92 tmpl=`cache: yarn`

**predicted_cluster_examples (head)**
- `Cache Size: ~1216 MB (1274821257 B)`
- `Cache Size: ~448 MB (470082938 B)`
- `Cache Size: ~1216 MB (1274692111 B)`

## #20 | TOP1_OK

- true_cluster_id: 116
- predicted_cluster_id: 116
- topk: 5

**base_log**
```
Cache Size: ~1216 MB (1274821257 B)
```

**mutated_log**
```
Cache Size: ~7698 MB (1274821257 B)
```

**top_matches**
- score=1.0000 tag=116 cid=116 tmpl=`Cache Size: ~1216 MB (1274821257 B)`
- score=0.9708 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9490 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`
- score=0.9474 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9450 tag=92 cid=92 tmpl=`cache: yarn`

**predicted_cluster_examples (head)**
- `Cache Size: ~1216 MB (1274821257 B)`
- `Cache Size: ~448 MB (470082938 B)`
- `Cache Size: ~1216 MB (1274692111 B)`

## #21 | TOPK_OK

- true_cluster_id: 140
- predicted_cluster_id: 68
- topk: 5

**log**
```
warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"
```

**top_matches**
- score=0.8584 tag=68 cid=68 tmpl=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.8576 tag=156 cid=156 tmpl=`Running: mkdir -p ./compiler/packages/babel-plugin-react-compiler/dist && echo "module.exports = require('../src/index.ts');" > ./compiler/p...`
- score=0.8535 tag=86 cid=86 tmpl=`git switch -`
- score=0.8530 tag=1 cid=1 tmpl=`﻿Current runner version: '2.328.0'`
- score=0.8517 tag=140 cid=140 tmpl=`warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"`
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"`

## #22 | TOPK_OK

- true_cluster_id: 140
- predicted_cluster_id: 156
- topk: 5

**base_log**
```
warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"
```

**mutated_log**
```
error Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.07.10"
```

**top_matches**
- score=0.8643 tag=156 cid=156 tmpl=`Running: mkdir -p ./compiler/packages/babel-plugin-react-compiler/dist && echo "module.exports = require('../src/index.ts');" > ./compiler/p...`
- score=0.8622 tag=68 cid=68 tmpl=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.8580 tag=140 cid=140 tmpl=`warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`
- score=0.8573 tag=86 cid=86 tmpl=`git switch -`
- score=0.8552 tag=1 cid=1 tmpl=`﻿Current runner version: '2.328.0'`

**predicted_cluster_examples (head)**
- `Running: mkdir -p ./compiler/packages/babel-plugin-react-compiler/dist && echo "module.exports = require('../src/index.ts');" > ./compiler/packages/babel-plugin-react-compiler/dist/index.js`

## #23 | TOP1_OK

- true_cluster_id: 169
- predicted_cluster_id: 169
- topk: 5

**base_log**
```
at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1
```

**mutated_log**
```
at file:///home/runner/work/react/react-new/fixtures/eslint-v7/build.mjs:10:1
```

**top_matches**
- score=0.9999 tag=169 cid=169 tmpl=`at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1`
- score=0.9720 tag=190 cid=190 tmpl=`BUILDING eslint-plugin-react-hooks.d.ts (cjs_dts)`
- score=0.9715 tag=191 cid=191 tmpl=`COMPLETE eslint-plugin-react-hooks.d.ts (cjs_dts)`
- score=0.9671 tag=164 cid=164 tmpl=`Error: Command failed: yarn build -r stable eslint-plugin-react-hooks`
- score=0.9657 tag=44 cid=44 tmpl=`Working directory is '/home/runner/work/react/react'`

**predicted_cluster_examples (head)**
- `at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`

## #24 | TOP1_OK

- true_cluster_id: 169
- predicted_cluster_id: 169
- topk: 5

**base_log**
```
at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1
```

**mutated_log**
```
at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:59:1
```

**top_matches**
- score=1.0000 tag=169 cid=169 tmpl=`at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1`
- score=0.9714 tag=190 cid=190 tmpl=`BUILDING eslint-plugin-react-hooks.d.ts (cjs_dts)`
- score=0.9707 tag=191 cid=191 tmpl=`COMPLETE eslint-plugin-react-hooks.d.ts (cjs_dts)`
- score=0.9679 tag=164 cid=164 tmpl=`Error: Command failed: yarn build -r stable eslint-plugin-react-hooks`
- score=0.9655 tag=44 cid=44 tmpl=`Working directory is '/home/runner/work/react/react'`

**predicted_cluster_examples (head)**
- `at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`

## #25 | MISS

- true_cluster_id: 176
- predicted_cluster_id: None
- topk: 5

**log**
```
pid: 2264,
```

## #26 | MISS

- true_cluster_id: 176
- predicted_cluster_id: None
- topk: 5

**log**
```
pid: 2264,
```

## #27 | TOP1_OK

- true_cluster_id: 195
- predicted_cluster_id: 195
- topk: 5

**log**
```
│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │
```

**top_matches**
- score=1.0000 tag=195 cid=195 tmpl=`│ eslint-plugin-react-hooks.development.js (NODE_DEV) │ 0 B │ 2.01 MB │ n/a │ 0 B │ 295.27 KB │ n/a │`
- score=0.9978 tag=155 cid=155 tmpl=`$ node ./scripts/rollup/build-all-release-channels.js -r stable eslint-plugin-react-hooks`
- score=0.9958 tag=187 cid=187 tmpl=`COMPLETE eslint-plugin-react-hooks.development.js (node_dev)`
- score=0.9955 tag=157 cid=157 tmpl=`BUILDING eslint-plugin-react-hooks.development.js (node_dev)`
- score=0.9947 tag=189 cid=189 tmpl=`COMPLETE eslint-plugin-react-hooks.production.js (node_prod)`

**predicted_cluster_examples (head)**
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.27 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

## #28 | TOP1_OK

- true_cluster_id: 195
- predicted_cluster_id: 195
- topk: 5

**base_log**
```
│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │
```

**mutated_log**
```
│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.0 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │
```

**top_matches**
- score=1.0000 tag=195 cid=195 tmpl=`│ eslint-plugin-react-hooks.development.js (NODE_DEV) │ 0 B │ 2.01 MB │ n/a │ 0 B │ 295.27 KB │ n/a │`
- score=0.9978 tag=155 cid=155 tmpl=`$ node ./scripts/rollup/build-all-release-channels.js -r stable eslint-plugin-react-hooks`
- score=0.9958 tag=187 cid=187 tmpl=`COMPLETE eslint-plugin-react-hooks.development.js (node_dev)`
- score=0.9955 tag=157 cid=157 tmpl=`BUILDING eslint-plugin-react-hooks.development.js (node_dev)`
- score=0.9947 tag=189 cid=189 tmpl=`COMPLETE eslint-plugin-react-hooks.production.js (node_prod)`

**predicted_cluster_examples (head)**
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.27 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

## #29 | TOP1_OK

- true_cluster_id: 4
- predicted_cluster_id: 4
- topk: 5

**base_log**
```
Version: 20250829.383
```

**mutated_log**
```
Version: 20250829.698
```

**top_matches**
- score=1.0000 tag=4 cid=4 tmpl=`Version: 20250829.383`
- score=0.8543 tag=46 cid=46 tmpl=`git version 2.51.0`
- score=0.7972 tag=1 cid=1 tmpl=`﻿Current runner version: '2.328.0'`
- score=0.7788 tag=167 cid=167 tmpl=`at checkExecSyncError (node:child_process:891:11)`
- score=0.7749 tag=43 cid=43 tmpl=`##[group]Getting Git version info`

**predicted_cluster_examples (head)**
- `Version: 20250829.383`
- `Version: 20250831.1.0`
- `Version: 20250908.385`

## #30 | TOP1_OK

- true_cluster_id: 4
- predicted_cluster_id: 4
- topk: 5

**base_log**
```
Version: 20250829.383
```

**mutated_log**
```
Version: 20250829.382
```

**top_matches**
- score=1.0000 tag=4 cid=4 tmpl=`Version: 20250829.383`
- score=0.8543 tag=46 cid=46 tmpl=`git version 2.51.0`
- score=0.7972 tag=1 cid=1 tmpl=`﻿Current runner version: '2.328.0'`
- score=0.7788 tag=167 cid=167 tmpl=`at checkExecSyncError (node:child_process:891:11)`
- score=0.7749 tag=43 cid=43 tmpl=`##[group]Getting Git version info`

**predicted_cluster_examples (head)**
- `Version: 20250829.383`
- `Version: 20250831.1.0`
- `Version: 20250908.385`

## #31 | MISS

- true_cluster_id: 22
- predicted_cluster_id: 114
- topk: 5

**log**
```
Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)
```

**top_matches**
- score=0.9894 tag=114 cid=114 tmpl=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9867 tag=119 cid=119 tmpl=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9840 tag=180 cid=180 tmpl=`Node.js v20.19.0`
- score=0.9835 tag=200 cid=200 tmpl=`Cache hit occurred on the primary key node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4, not saving...`
- score=0.9759 tag=142 cid=142 tmpl=`$ node ./scripts/flow/createFlowConfigs.js`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #32 | MISS

- true_cluster_id: 22
- predicted_cluster_id: 114
- topk: 5

**base_log**
```
Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)
```

**mutated_log**
```
Error: Download action repository 'actions/setup-node@v4' (SHA:01fa9e1d6240cda060036369853fc208e384b348)
```

**top_matches**
- score=0.9927 tag=114 cid=114 tmpl=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9908 tag=119 cid=119 tmpl=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9886 tag=200 cid=200 tmpl=`Cache hit occurred on the primary key node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4, not saving...`
- score=0.9862 tag=180 cid=180 tmpl=`Node.js v20.19.0`
- score=0.9731 tag=142 cid=142 tmpl=`$ node ./scripts/flow/createFlowConfigs.js`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #33 | TOP1_OK

- true_cluster_id: 24
- predicted_cluster_id: 24
- topk: 5

**base_log**
```
##[group]Run actions/checkout@v4
```

**mutated_log**
```
##[group]Run actions/checkout@v8
```

**top_matches**
- score=1.0000 tag=24 cid=24 tmpl=`##[group]Run actions/checkout@v4`
- score=0.9187 tag=147 cid=147 tmpl=`##[group]Run yarn --frozen-lockfile`
- score=0.9058 tag=55 cid=55 tmpl=`hint: of your new repositories, which will suppress this warning, call:`
- score=0.9055 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9044 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `##[group]Run actions/checkout@v4`
- `##[group]Run actions/setup-node@v4`
- `##[group]Run actions/cache@v4`

## #34 | TOP1_OK

- true_cluster_id: 24
- predicted_cluster_id: 24
- topk: 5

**log**
```
##[group]Run actions/checkout@v4
```

**top_matches**
- score=1.0000 tag=24 cid=24 tmpl=`##[group]Run actions/checkout@v4`
- score=0.9187 tag=147 cid=147 tmpl=`##[group]Run yarn --frozen-lockfile`
- score=0.9058 tag=55 cid=55 tmpl=`hint: of your new repositories, which will suppress this warning, call:`
- score=0.9055 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9044 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `##[group]Run actions/checkout@v4`
- `##[group]Run actions/setup-node@v4`
- `##[group]Run actions/cache@v4`

## #35 | TOP1_OK

- true_cluster_id: 65
- predicted_cluster_id: 65
- topk: 5

**base_log**
```
[command]/usr/bin/git config --local gc.auto 0
```

**mutated_log**
```
[command]/usr/bin/git-x86_64 config --local gc.auto 0
```

**top_matches**
- score=0.9990 tag=65 cid=65 tmpl=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9985 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`
- score=0.9980 tag=69 cid=69 tmpl=`[command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***`
- score=0.9973 tag=75 cid=75 tmpl=`[command]/usr/bin/git sparse-checkout disable`
- score=0.9956 tag=108 cid=108 tmpl=`[command]/usr/local/bin/yarn --version`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local gc.auto 0`
- `[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- `[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`

## #36 | TOP1_OK

- true_cluster_id: 65
- predicted_cluster_id: 65
- topk: 5

**base_log**
```
[command]/usr/bin/git config --local gc.auto 0
```

**mutated_log**
```
[command]/usr/bin-new/git config --local gc.auto 9
```

**top_matches**
- score=0.9992 tag=65 cid=65 tmpl=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9989 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`
- score=0.9984 tag=69 cid=69 tmpl=`[command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***`
- score=0.9977 tag=75 cid=75 tmpl=`[command]/usr/bin/git sparse-checkout disable`
- score=0.9970 tag=108 cid=108 tmpl=`[command]/usr/local/bin/yarn --version`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local gc.auto 0`
- `[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- `[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`

## #37 | TOPK_OK

- true_cluster_id: 5
- predicted_cluster_id: 22
- topk: 5

**base_log**
```
Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056
```

**mutated_log**
```
Commit: cfce01a78eb455f23de9981e2e79cb8dc83e6056
```

**top_matches**
- score=0.9688 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9683 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9525 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9439 tag=116 cid=116 tmpl=`Cache Size: ~1216 MB (1274821257 B)`
- score=0.9342 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`

**predicted_cluster_examples (head)**
- `Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- `Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- `Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`

## #38 | TOPK_OK

- true_cluster_id: 5
- predicted_cluster_id: 22
- topk: 5

**log**
```
Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056
```

**top_matches**
- score=0.9688 tag=22 cid=22 tmpl=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9683 tag=5 cid=5 tmpl=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9525 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9439 tag=116 cid=116 tmpl=`Cache Size: ~1216 MB (1274821257 B)`
- score=0.9342 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`

**predicted_cluster_examples (head)**
- `Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- `Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- `Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`

## #39 | TOPK_OK

- true_cluster_id: 18
- predicted_cluster_id: 208
- topk: 5

**log**
```
Secret source: None
```

**top_matches**
- score=0.8665 tag=208 cid=208 tmpl=`'react-hooks/no-unused-directives': 'error',`
- score=0.8595 tag=86 cid=86 tmpl=`git switch -`
- score=0.8493 tag=18 cid=18 tmpl=`Secret source: Actions`
- score=0.8417 tag=138 cid=138 tmpl=`yarn install v1.22.22`
- score=0.8367 tag=43 cid=43 tmpl=`##[group]Getting Git version info`

**predicted_cluster_examples (head)**
- `'react-hooks/no-unused-directives': 'error',`

## #40 | TOPK_OK

- true_cluster_id: 18
- predicted_cluster_id: 208
- topk: 5

**log**
```
Secret source: None
```

**top_matches**
- score=0.8665 tag=208 cid=208 tmpl=`'react-hooks/no-unused-directives': 'error',`
- score=0.8595 tag=86 cid=86 tmpl=`git switch -`
- score=0.8493 tag=18 cid=18 tmpl=`Secret source: Actions`
- score=0.8417 tag=138 cid=138 tmpl=`yarn install v1.22.22`
- score=0.8367 tag=43 cid=43 tmpl=`##[group]Getting Git version info`

**predicted_cluster_examples (head)**
- `'react-hooks/no-unused-directives': 'error',`

## #41 | TOPK_OK

- true_cluster_id: 26
- predicted_cluster_id: 90
- topk: 5

**base_log**
```
ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**mutated_log**
```
ref: bc493f719529ca9d33ffaa3f3fd19a45c222671c
```

**top_matches**
- score=0.9914 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9909 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9872 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9745 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9658 tag=115 cid=115 tmpl=`Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`

**predicted_cluster_examples (head)**
- `07e437c198be972d7c15ad8f32ada4dfec3985a1`

## #42 | TOP1_OK

- true_cluster_id: 26
- predicted_cluster_id: 26
- topk: 5

**log**
```
ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9994 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9979 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9797 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9769 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`

**predicted_cluster_examples (head)**
- `ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `ref: 71802995908aa85f00c80e117c635c5dbe28c45c`

## #43 | MISS

- true_cluster_id: 67
- predicted_cluster_id: 89
- topk: 5

**log**
```
[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
```

**top_matches**
- score=0.9940 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9936 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9858 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`
- score=0.9851 tag=75 cid=75 tmpl=`[command]/usr/bin/git sparse-checkout disable`
- score=0.9833 tag=69 cid=69 tmpl=`[command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git log -1 --format=%H`

## #44 | MISS

- true_cluster_id: 67
- predicted_cluster_id: 112
- topk: 5

**base_log**
```
[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
```

**mutated_log**
```
[command]/usr/bin_v2/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
```

**top_matches**
- score=0.9919 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9906 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9798 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`
- score=0.9797 tag=75 cid=75 tmpl=`[command]/usr/bin/git sparse-checkout disable`
- score=0.9769 tag=69 cid=69 tmpl=`[command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***`

**predicted_cluster_examples (head)**
- `[command]/usr/local/bin/yarn config get enableGlobalCache`

## #45 | MISS

- true_cluster_id: 68
- predicted_cluster_id: 89
- topk: 5

**log**
```
[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
```

**top_matches**
- score=0.9787 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9615 tag=67 cid=67 tmpl=`[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`
- score=0.9563 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9533 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9456 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git log -1 --format=%H`

## #46 | MISS

- true_cluster_id: 68
- predicted_cluster_id: 89
- topk: 5

**base_log**
```
[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
```

**mutated_log**
```
Error: [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
```

**top_matches**
- score=0.9712 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9634 tag=67 cid=67 tmpl=`[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`
- score=0.9607 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9512 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9342 tag=45 cid=45 tmpl=`[command]/usr/bin/git version`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git log -1 --format=%H`

## #47 | TOP1_OK

- true_cluster_id: 71
- predicted_cluster_id: 71
- topk: 5

**log**
```
[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=71 cid=71 tmpl=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`
- score=0.9520 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9435 tag=57 cid=57 tmpl=`hint: git config --global init.defaultBranch <name>`
- score=0.9406 tag=84 cid=84 tmpl=`git switch -c <new-branch-name>`
- score=0.9283 tag=107 cid=107 tmpl=`yarn: 1.22.22`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 71802995908aa85f00c80e117c635c5dbe28c45c`

## #48 | TOP1_OK

- true_cluster_id: 71
- predicted_cluster_id: 71
- topk: 5

**log**
```
[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=71 cid=71 tmpl=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`
- score=0.9520 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9435 tag=57 cid=57 tmpl=`hint: git config --global init.defaultBranch <name>`
- score=0.9406 tag=84 cid=84 tmpl=`git switch -c <new-branch-name>`
- score=0.9283 tag=107 cid=107 tmpl=`yarn: 1.22.22`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 71802995908aa85f00c80e117c635c5dbe28c45c`

## #49 | MISS

- true_cluster_id: 73
- predicted_cluster_id: 138
- topk: 5

**base_log**
```
* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD
```

**mutated_log**
```
* branch            63fc8616436ecb43f4cdfaff670aaa1484c9f221 -> FETCH_HEAD
```

**top_matches**
- score=0.9598 tag=138 cid=138 tmpl=`yarn install v1.22.22`
- score=0.9594 tag=115 cid=115 tmpl=`Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- score=0.9591 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9540 tag=47 cid=47 tmpl=`Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- score=0.9518 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`

**predicted_cluster_examples (head)**
- `yarn install v1.22.22`
- `yarn run v1.22.22`

## #50 | TOP1_OK

- true_cluster_id: 73
- predicted_cluster_id: 73
- topk: 5

**base_log**
```
* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD
```

**mutated_log**
```
* branch            07e437c040be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD
```

**top_matches**
- score=1.0000 tag=73 cid=73 tmpl=`* branch 07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9988 tag=90 cid=90 tmpl=`07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9979 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9825 tag=115 cid=115 tmpl=`Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- score=0.9810 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`

**predicted_cluster_examples (head)**
- `* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- `* branch            71802995908aa85f00c80e117c635c5dbe28c45c -> FETCH_HEAD`

## #51 | TOP1_OK

- true_cluster_id: 77
- predicted_cluster_id: 77
- topk: 5

**base_log**
```
[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c
```

**mutated_log**
```
Error: [command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe58c45c
```

**top_matches**
- score=0.9896 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9406 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9290 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9089 tag=201 cid=201 tmpl=`Sent 2463620 of 472225668 (0.5%), 2.3 MBs/sec`
- score=0.9052 tag=67 cid=67 tmpl=`[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`

## #52 | TOP1_OK

- true_cluster_id: 77
- predicted_cluster_id: 77
- topk: 5

**base_log**
```
[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c
```

**mutated_log**
```
[command]/usr/bin/git checkout --progress --force 22d69dfc700598a2f89dcc15479a11fd4f24bd1e
```

**top_matches**
- score=0.9921 tag=77 cid=77 tmpl=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9744 tag=112 cid=112 tmpl=`[command]/usr/local/bin/yarn config get enableGlobalCache`
- score=0.9573 tag=89 cid=89 tmpl=`[command]/usr/bin/git log -1 --format=%H`
- score=0.9483 tag=110 cid=110 tmpl=`[command]/usr/local/bin/yarn cache dir`
- score=0.9464 tag=75 cid=75 tmpl=`[command]/usr/bin/git sparse-checkout disable`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`

## #53 | TOP1_OK

- true_cluster_id: 78
- predicted_cluster_id: 78
- topk: 5

**log**
```
Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.
```

**top_matches**
- score=0.9874 tag=78 cid=78 tmpl=`Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- score=0.9625 tag=158 cid=158 tmpl=`@rollup/plugin-typescript TS2345: Argument of type 'ErrorSeverity.Off' is not assignable to parameter of type 'never'.`
- score=0.9092 tag=82 cid=82 tmpl=`If you want to create a new branch to retain commits you create, you may`
- score=0.9074 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9048 tag=199 cid=199 tmpl=`Failed to save: Unable to reserve cache with key runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d361...`

**predicted_cluster_examples (head)**
- `Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- `Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`

## #54 | TOP1_OK

- true_cluster_id: 78
- predicted_cluster_id: 78
- topk: 5

**log**
```
Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.
```

**top_matches**
- score=0.9874 tag=78 cid=78 tmpl=`Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- score=0.9625 tag=158 cid=158 tmpl=`@rollup/plugin-typescript TS2345: Argument of type 'ErrorSeverity.Off' is not assignable to parameter of type 'never'.`
- score=0.9092 tag=82 cid=82 tmpl=`If you want to create a new branch to retain commits you create, you may`
- score=0.9074 tag=26 cid=26 tmpl=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9048 tag=199 cid=199 tmpl=`Failed to save: Unable to reserve cache with key runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d361...`

**predicted_cluster_examples (head)**
- `Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- `Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`

## #55 | TOP1_OK

- true_cluster_id: 114
- predicted_cluster_id: 114
- topk: 5

**log**
```
Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4
```

**top_matches**
- score=1.0000 tag=114 cid=114 tmpl=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9990 tag=119 cid=119 tmpl=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9982 tag=200 cid=200 tmpl=`Cache hit occurred on the primary key node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4, not saving...`
- score=0.9724 tag=180 cid=180 tmpl=`Node.js v20.19.0`
- score=0.9550 tag=142 cid=142 tmpl=`$ node ./scripts/flow/createFlowConfigs.js`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #56 | TOP1_OK

- true_cluster_id: 114
- predicted_cluster_id: 114
- topk: 5

**base_log**
```
Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4
```

**mutated_log**
```
Cache hit for: node-cache-Linux-x64-yarn-a3b6cf31ea394c9361ceb6eb211f80672d934dd23d23d40edd0fa82b23b0bb50
```

**top_matches**
- score=0.9680 tag=114 cid=114 tmpl=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9633 tag=200 cid=200 tmpl=`Cache hit occurred on the primary key node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4, not saving...`
- score=0.9620 tag=119 cid=119 tmpl=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9593 tag=102 cid=102 tmpl=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc ...`
- score=0.9477 tag=6 cid=6 tmpl=`Build Date:`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #57 | MISS

- true_cluster_id: 119
- predicted_cluster_id: 121
- topk: 5

**base_log**
```
Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**mutated_log**
```
Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-606309b0745e3fb8406baf99a52395c447a7759bd140c224d9d4d9b27eb1cd0d
```

**top_matches**
- score=0.9985 tag=121 cid=121 tmpl=`key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9984 tag=132 cid=132 tmpl=`Cache not found for input keys: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d35...`
- score=0.9636 tag=199 cid=199 tmpl=`Failed to save: Unable to reserve cache with key runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d361...`
- score=0.9633 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9532 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #58 | MISS

- true_cluster_id: 119
- predicted_cluster_id: 121
- topk: 5

**log**
```
Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**top_matches**
- score=0.9999 tag=121 cid=121 tmpl=`key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9998 tag=132 cid=132 tmpl=`Cache not found for input keys: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d35...`
- score=0.9721 tag=199 cid=199 tmpl=`Failed to save: Unable to reserve cache with key runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d361...`
- score=0.9714 tag=128 cid=128 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-...`
- score=0.9612 tag=127 cid=127 tmpl=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #59 | TOP1_OK

- true_cluster_id: 138
- predicted_cluster_id: 138
- topk: 5

**base_log**
```
yarn run v1.22.22
```

**mutated_log**
```
yarn run v2.47.22
```

**top_matches**
- score=0.9689 tag=138 cid=138 tmpl=`yarn install v1.22.22`
- score=0.9484 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`
- score=0.9382 tag=61 cid=61 tmpl=`hint: Disable this message with "git config set advice.defaultBranchName false"`
- score=0.9236 tag=93 cid=93 tmpl=`cache-dependency-path: yarn.lock`
- score=0.9209 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `yarn install v1.22.22`
- `yarn run v1.22.22`

## #60 | TOP1_OK

- true_cluster_id: 138
- predicted_cluster_id: 138
- topk: 5

**base_log**
```
yarn run v1.22.22
```

**mutated_log**
```
yarn run v1.22.23
```

**top_matches**
- score=0.9689 tag=138 cid=138 tmpl=`yarn install v1.22.22`
- score=0.9484 tag=111 cid=111 tmpl=`/home/runner/.cache/yarn/v6`
- score=0.9382 tag=61 cid=61 tmpl=`hint: Disable this message with "git config set advice.defaultBranchName false"`
- score=0.9236 tag=93 cid=93 tmpl=`cache-dependency-path: yarn.lock`
- score=0.9209 tag=129 cid=129 tmpl=`﻿/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`

**predicted_cluster_examples (head)**
- `yarn install v1.22.22`
- `yarn run v1.22.22`
