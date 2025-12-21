# dec2vec Robustness Report (RAW KB): maryangel101_dec2vec_robustness_rawkb_seed0.jsonl

- total: 60
- hit@1: 57 (0.9500)
- hit@k: 57 (0.9500)

## #1 | TOP1_OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- topk: 5

**log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json’: No such file or directory
```

**top_matches**
- score=0.9868 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9868 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9868 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`
- score=0.9775 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9715 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #2 | TOP1_OK

- true_cluster_id: 128
- predicted_cluster_id: 128
- topk: 5

**base_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json’: No such file or directory
```

**mutated_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json:_v2 Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/@babel/core/node_modules/@babel/generator/package.json’: No such file or directory
```

**top_matches**
- score=0.9869 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9869 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`
- score=0.9868 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9776 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9715 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/README.md: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/README.md’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/LICENSE’: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js: Cannot hard link to ‘compiler/node_modules/babel-plugin-react-compiler/node_modules/jest/bin/jest.js’: No such file or directory`

## #3 | TOP1_OK

- true_cluster_id: 127
- predicted_cluster_id: 127
- topk: 5

**base_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-message-util/node_modules/@jest/types/node_modules/@sinclair/typebox: Cannot mkdir: No such file or directory
```

**mutated_log**
```
Error: /usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-message-util/node_modules/@jest/types/node_modules/@sinclair/typebox: Cannot mkdir: No such file or directory
```

**top_matches**
- score=0.9943 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`
- score=0.9932 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9865 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9801 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9786 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin: Cannot mkdir: No such file or directory`

## #4 | TOP1_OK

- true_cluster_id: 127
- predicted_cluster_id: 127
- topk: 5

**base_log**
```
/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-message-util/node_modules/@jest/types/node_modules/@sinclair/typebox: Cannot mkdir: No such file or directory
```

**mutated_log**
```
Error: /usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-message-util/node_modules/@jest/types/node_modules/@sinclair/typebox: Cannot mkdir: No such file or directory
```

**top_matches**
- score=0.9943 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`
- score=0.9932 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9865 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9801 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9786 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest: Cannot mkdir: No such file or directory`
- `/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest/bin: Cannot mkdir: No such file or directory`

## #5 | TOP1_OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- topk: 5

**log**
```
Received 432013312 of 1274692111 (33.9%), 103.0 MBs/sec
```

**top_matches**
- score=1.0000 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=1.0000 tag=115:1 cid=115 text=`Received 1274821257 of 1274821257 (100.0%), 152.5 MBs/sec`
- score=1.0000 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`
- score=0.9825 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9768 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`
- `Received 264241152 of 1274821257 (20.7%), 84.0 MBs/sec`

## #6 | TOP1_OK

- true_cluster_id: 115
- predicted_cluster_id: 115
- topk: 5

**log**
```
Received 432013312 of 1274692111 (33.9%), 103.0 MBs/sec
```

**top_matches**
- score=1.0000 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=1.0000 tag=115:1 cid=115 text=`Received 1274821257 of 1274821257 (100.0%), 152.5 MBs/sec`
- score=1.0000 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`
- score=0.9825 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9768 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`

**predicted_cluster_examples (head)**
- `Received 4194304 of 1274821257 (0.3%), 4.0 MBs/sec`
- `Received 134217728 of 1274821257 (10.5%), 64.0 MBs/sec`
- `Received 264241152 of 1274821257 (20.7%), 84.0 MBs/sec`

## #7 | MISS

- true_cluster_id: 144
- predicted_cluster_id: 47
- topk: 5

**base_log**
```
Done in 1.17s.
```

**mutated_log**
```
Error: Done in 1.94s.
```

**top_matches**
- score=0.8487 tag=47:1 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes`
- score=0.8457 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.8240 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.8180 tag=78:0 cid=78 text=`Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`
- score=0.7954 tag=78:1 cid=78 text=`Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`

**predicted_cluster_examples (head)**
- `Temporarily overriding HOME='/home/runner/work/_temp/3fe31285-97b1-4d9d-9cee-5b0ff64e79a3' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/0f5c664f-5b52-45ed-9fa6-dd937c2019ed' before making global git config changes`
- `Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`

## #8 | TOP1_OK

- true_cluster_id: 144
- predicted_cluster_id: 144
- topk: 5

**log**
```
Done in 1.17s.
```

**top_matches**
- score=1.0000 tag=144:1 cid=144 text=`Done in 0.81s.`
- score=1.0000 tag=144:2 cid=144 text=`Done in 0.83s.`
- score=1.0000 tag=144:0 cid=144 text=`Done in 0.92s.`
- score=0.2873 tag=18:0 cid=18 text=`Secret source: Actions`
- score=0.1902 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`

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
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig
```

**top_matches**
- score=1.0000 tag=143:0 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig`
- score=0.9998 tag=143:2 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser-esm/.flowconfig`
- score=0.9997 tag=143:1 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/test/.flowconfig`
- score=0.9407 tag=169:0 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`
- score=0.9407 tag=169:1 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`

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
Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig
```

**top_matches**
- score=1.0000 tag=143:0 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig`
- score=0.9998 tag=143:2 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser-esm/.flowconfig`
- score=0.9997 tag=143:1 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/test/.flowconfig`
- score=0.9407 tag=169:0 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`
- score=0.9407 tag=169:1 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`

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
Temporarily overriding HOME='/home/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes
```

**mutated_log**
```
Temporarily overriding HOME='/home/runner-new/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes
```

**top_matches**
- score=0.9989 tag=47:1 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes`
- score=0.9871 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9514 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`
- score=0.9498 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9474 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`

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
Temporarily overriding HOME='/home/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes
```

**mutated_log**
```
Temporarily overriding HOME='/home-new/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes
```

**top_matches**
- score=0.9989 tag=47:1 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/508dd31f-bd40-4ece-a944-22d3bfbfa6a1' before making global git config changes`
- score=0.9871 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9514 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`
- score=0.9498 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9474 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`

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
[command]/usr/bin/tar -xf /home/runner/work/_temp/b6d06499-dda1-42f5-9552-8f6aa9b5db7c/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**mutated_log**
```
Error: [command]/usr/bin/tar -xf /home/runner/work/_temp/34712036-3c2b-3106-53f6-10d382729bd5/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**top_matches**
- score=0.9976 tag=117:2 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/432e34ef-7086-40c7-a99b-9e7e62f3b16d/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9943 tag=117:0 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/ff8d8d03-59a0-4b71-a5d2-ed7fc14ab628/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9876 tag=117:1 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/31bf3d69-0d40-4086-a0b9-41d9b019d0fd/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9461 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`
- score=0.9445 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/6fe4625a-4086-40e6-a910-3e916ffb47fa/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/f7f85e1c-6683-45b8-b1f4-3b683d246791/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/da668ef2-09dd-4b0f-ab03-20889d1c5c95/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`

## #14 | TOP1_OK

- true_cluster_id: 117
- predicted_cluster_id: 117
- topk: 5

**log**
```
[command]/usr/bin/tar -xf /home/runner/work/_temp/b6d06499-dda1-42f5-9552-8f6aa9b5db7c/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd
```

**top_matches**
- score=0.9981 tag=117:2 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/432e34ef-7086-40c7-a99b-9e7e62f3b16d/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9945 tag=117:0 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/ff8d8d03-59a0-4b71-a5d2-ed7fc14ab628/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9882 tag=117:1 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/31bf3d69-0d40-4086-a0b9-41d9b019d0fd/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9458 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`
- score=0.9442 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/6fe4625a-4086-40e6-a910-3e916ffb47fa/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/f7f85e1c-6683-45b8-b1f4-3b683d246791/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`
- `[command]/usr/bin/tar -xf /home/runner/work/_temp/da668ef2-09dd-4b0f-ab03-20889d1c5c95/cache.tzst -P -C /home/runner/work/react/react --use-compress-program unzstd`

## #15 | TOP1_OK

- true_cluster_id: 102
- predicted_cluster_id: 102
- topk: 5

**log**
```
[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f -f /home/runner/work/_temp/9a2c2823-3759-4112-87b9-a4e6a9dd307d
```

**top_matches**
- score=1.0000 tag=102:1 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f ...`
- score=0.9990 tag=102:0 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/a9aad03f-00b4-46e3-9e7a-338e0c8b4bc9 ...`
- score=0.9963 tag=102:2 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/502712a1-1624-4483-ad36-5c994752e130 ...`
- score=0.9493 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9421 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`

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
[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f -f /home/runner/work/_temp/9a2c2823-3759-4112-87b9-a4e6a9dd307d
```

**mutated_log**
```
[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner_backup/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f -f /home/runner/work/_temp/9a2c2823-3759-4112-87b9-a4e6a9dd307d
```

**top_matches**
- score=1.0000 tag=102:1 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f ...`
- score=0.9990 tag=102:0 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/a9aad03f-00b4-46e3-9e7a-338e0c8b4bc9 ...`
- score=0.9963 tag=102:2 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/502712a1-1624-4483-ad36-5c994752e130 ...`
- score=0.9493 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9421 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6432c209-1293-4d97-8c8d-f0fe86dac4cc -f /home/runner/work/_temp/1a1c40e2-9dbf-49f3-ac81-2bbf2d87c2a4`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/68d379ce-4198-47ac-b596-b8c0c46bcde9 -f /home/runner/work/_temp/6e116644-cc24-4003-9c50-2763c2b47a52`
- `[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/27b98926-9f2d-42d4-ab15-25d4938652d6 -f /home/runner/work/_temp/446bb931-0937-4eec-8e1e-a072e8c51220`

## #17 | TOP1_OK

- true_cluster_id: 23
- predicted_cluster_id: 23
- topk: 5

**log**
```
Complete job name: ESLint v6
```

**top_matches**
- score=1.0000 tag=23:2 cid=23 text=`Complete job name: ESLint v7`
- score=1.0000 tag=23:0 cid=23 text=`Complete job name: ESLint v8`
- score=1.0000 tag=23:1 cid=23 text=`Complete job name: ESLint v9`
- score=0.9585 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9575 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`

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
Complete job name: ESLint v6
```

**top_matches**
- score=1.0000 tag=23:2 cid=23 text=`Complete job name: ESLint v7`
- score=1.0000 tag=23:0 cid=23 text=`Complete job name: ESLint v8`
- score=1.0000 tag=23:1 cid=23 text=`Complete job name: ESLint v9`
- score=0.9585 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9575 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`

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
Cache Size: ~448 MB (470082938 B)
```

**top_matches**
- score=1.0000 tag=116:2 cid=116 text=`Cache Size: ~448 MB (470082938 B)`
- score=1.0000 tag=116:0 cid=116 text=`Cache Size: ~1216 MB (1274821257 B)`
- score=1.0000 tag=116:1 cid=116 text=`Cache Size: ~1216 MB (1274692111 B)`
- score=0.9708 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9474 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`

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
Cache Size: ~448 MB (470082938 B)
```

**mutated_log**
```
Cache Size: ~225 MB (470082938 B)
```

**top_matches**
- score=1.0000 tag=116:2 cid=116 text=`Cache Size: ~448 MB (470082938 B)`
- score=1.0000 tag=116:0 cid=116 text=`Cache Size: ~1216 MB (1274821257 B)`
- score=1.0000 tag=116:1 cid=116 text=`Cache Size: ~1216 MB (1274692111 B)`
- score=0.9708 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9474 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`

**predicted_cluster_examples (head)**
- `Cache Size: ~1216 MB (1274821257 B)`
- `Cache Size: ~448 MB (470082938 B)`
- `Cache Size: ~1216 MB (1274692111 B)`

## #21 | TOP1_OK

- true_cluster_id: 140
- predicted_cluster_id: 140
- topk: 5

**log**
```
warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"
```

**top_matches**
- score=1.0000 tag=140:0 cid=140 text=`warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.27.1"`
- score=1.0000 tag=140:1 cid=140 text=`warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"`
- score=0.8584 tag=68:1 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.8517 tag=140:2 cid=140 text=`warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`
- score=0.8347 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`

**predicted_cluster_examples (head)**
- `warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`
- `warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.27.0"`
- `warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"`

## #22 | TOP1_OK

- true_cluster_id: 140
- predicted_cluster_id: 140
- topk: 5

**base_log**
```
warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"
```

**mutated_log**
```
error Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"
```

**top_matches**
- score=0.9998 tag=140:0 cid=140 text=`warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.27.1"`
- score=0.9998 tag=140:1 cid=140 text=`warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"`
- score=0.8622 tag=68:1 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.8580 tag=140:2 cid=140 text=`warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`
- score=0.8397 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`

**predicted_cluster_examples (head)**
- `warning Resolution field "jsdom@22.1.0" is incompatible with requested version "jsdom@^20.0.0"`
- `warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.27.0"`
- `warning Resolution field "@babel/types@7.26.3" is incompatible with requested version "@babel/types@^7.26.10"`

## #23 | TOP1_OK

- true_cluster_id: 169
- predicted_cluster_id: 169
- topk: 5

**base_log**
```
at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1
```

**mutated_log**
```
at file:///home/runner/work/react/react/fixtures/eslint-v6_backup/build.mjs:10:0
```

**top_matches**
- score=1.0000 tag=169:1 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`
- score=1.0000 tag=169:2 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v9/build.mjs:10:1`
- score=1.0000 tag=169:0 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`
- score=0.9435 tag=143:2 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser-esm/.flowconfig`
- score=0.9407 tag=143:0 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig`

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
at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1
```

**mutated_log**
```
at file:///home/runner/work/react/react/fixtures_v2/eslint-v6/build.mjs:10:1
```

**top_matches**
- score=0.9999 tag=169:1 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`
- score=0.9999 tag=169:2 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v9/build.mjs:10:1`
- score=0.9999 tag=169:0 cid=169 text=`at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`
- score=0.9429 tag=143:2 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-browser-esm/.flowconfig`
- score=0.9400 tag=143:0 cid=143 text=`Wrote a Flow config to /home/runner/work/react/react/scripts/flow/dom-edge-parcel/.flowconfig`

**predicted_cluster_examples (head)**
- `at file:///home/runner/work/react/react/fixtures/eslint-v7/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v8/build.mjs:10:1`
- `at file:///home/runner/work/react/react/fixtures/eslint-v6/build.mjs:10:1`

## #25 | MISS

- true_cluster_id: 176
- predicted_cluster_id: None
- topk: 5

**base_log**
```
pid: 2264,
```

**mutated_log**
```
pid: 7594,
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
│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │
```

**top_matches**
- score=1.0000 tag=195:2 cid=195 text=`│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │`
- score=1.0000 tag=195:0 cid=195 text=`│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.3 KB     │ n/a  │`
- score=0.9998 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`
- score=0.9489 tag=117:0 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/ff8d8d03-59a0-4b71-a5d2-ed7fc14ab628/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9476 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`

**predicted_cluster_examples (head)**
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.27 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │`
- `│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

## #28 | TOP1_OK

- true_cluster_id: 195
- predicted_cluster_id: 195
- topk: 5

**log**
```
│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │
```

**top_matches**
- score=1.0000 tag=195:2 cid=195 text=`│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.28 KB    │ n/a  │`
- score=1.0000 tag=195:0 cid=195 text=`│ eslint-plugin-react-hooks.production.js  (NODE_PROD) │ 0 B       │ 2 MB         │ n/a  │ 0 B       │ 294.3 KB     │ n/a  │`
- score=0.9998 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`
- score=0.9489 tag=117:0 cid=117 text=`[command]/usr/bin/tar -xf /home/runner/work/_temp/ff8d8d03-59a0-4b71-a5d2-ed7fc14ab628/cache.tzst -P -C /home/runner/work/react/react --use-...`
- score=0.9476 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`

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
Version: 20250829.233
```

**top_matches**
- score=1.0000 tag=4:2 cid=4 text=`Version: 20250831.1.0`
- score=1.0000 tag=4:1 cid=4 text=`Version: 20250908.385`
- score=1.0000 tag=4:0 cid=4 text=`Version: 20250829.383`
- score=0.7541 tag=24:1 cid=24 text=`##[group]Run actions/setup-node@v4`
- score=0.7123 tag=18:1 cid=18 text=`Secret source: None`

**predicted_cluster_examples (head)**
- `Version: 20250829.383`
- `Version: 20250831.1.0`
- `Version: 20250908.385`

## #30 | TOP1_OK

- true_cluster_id: 4
- predicted_cluster_id: 4
- topk: 5

**log**
```
Version: 20250829.383
```

**top_matches**
- score=1.0000 tag=4:2 cid=4 text=`Version: 20250831.1.0`
- score=1.0000 tag=4:1 cid=4 text=`Version: 20250908.385`
- score=1.0000 tag=4:0 cid=4 text=`Version: 20250829.383`
- score=0.7541 tag=24:1 cid=24 text=`##[group]Run actions/setup-node@v4`
- score=0.7123 tag=18:1 cid=18 text=`Secret source: None`

**predicted_cluster_examples (head)**
- `Version: 20250829.383`
- `Version: 20250831.1.0`
- `Version: 20250908.385`

## #31 | TOP1_OK

- true_cluster_id: 22
- predicted_cluster_id: 22
- topk: 5

**log**
```
Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)
```

**top_matches**
- score=1.0000 tag=22:1 cid=22 text=`Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- score=0.9894 tag=114:1 cid=114 text=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9867 tag=119:0 cid=119 text=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9360 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9342 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`

**predicted_cluster_examples (head)**
- `Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- `Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- `Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`

## #32 | TOP1_OK

- true_cluster_id: 22
- predicted_cluster_id: 22
- topk: 5

**log**
```
Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)
```

**top_matches**
- score=1.0000 tag=22:1 cid=22 text=`Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- score=0.9894 tag=114:1 cid=114 text=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9867 tag=119:0 cid=119 text=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9360 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9342 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`

**predicted_cluster_examples (head)**
- `Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- `Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- `Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`

## #33 | TOP1_OK

- true_cluster_id: 24
- predicted_cluster_id: 24
- topk: 5

**log**
```
##[group]Run actions/setup-node@v4
```

**top_matches**
- score=1.0000 tag=24:1 cid=24 text=`##[group]Run actions/setup-node@v4`
- score=0.9313 tag=119:0 cid=119 text=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9277 tag=114:1 cid=114 text=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9196 tag=22:1 cid=22 text=`Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- score=0.8896 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

**predicted_cluster_examples (head)**
- `##[group]Run actions/checkout@v4`
- `##[group]Run actions/setup-node@v4`
- `##[group]Run actions/cache@v4`

## #34 | TOP1_OK

- true_cluster_id: 24
- predicted_cluster_id: 24
- topk: 5

**base_log**
```
##[group]Run actions/setup-node@v4
```

**mutated_log**
```
##[group]Run actions/setup-node@v1
```

**top_matches**
- score=1.0000 tag=24:1 cid=24 text=`##[group]Run actions/setup-node@v4`
- score=0.9313 tag=119:0 cid=119 text=`Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9277 tag=114:1 cid=114 text=`Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- score=0.9196 tag=22:1 cid=22 text=`Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)`
- score=0.8896 tag=195:1 cid=195 text=`│ eslint-plugin-react-hooks.development.js  (NODE_DEV) │ 0 B       │ 2.01 MB      │ n/a  │ 0 B       │ 295.28 KB    │ n/a  │`

**predicted_cluster_examples (head)**
- `##[group]Run actions/checkout@v4`
- `##[group]Run actions/setup-node@v4`
- `##[group]Run actions/cache@v4`

## #35 | TOP1_OK

- true_cluster_id: 65
- predicted_cluster_id: 65
- topk: 5

**log**
```
[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
```

**top_matches**
- score=1.0000 tag=65:2 cid=65 text=`[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`
- score=0.9992 tag=65:1 cid=65 text=`[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- score=0.9980 tag=65:0 cid=65 text=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9848 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9474 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local gc.auto 0`
- `[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- `[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`

## #36 | TOP1_OK

- true_cluster_id: 65
- predicted_cluster_id: 65
- topk: 5

**log**
```
[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
```

**top_matches**
- score=1.0000 tag=65:2 cid=65 text=`[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`
- score=0.9992 tag=65:1 cid=65 text=`[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- score=0.9980 tag=65:0 cid=65 text=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9848 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9474 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local gc.auto 0`
- `[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- `[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`

## #37 | TOP1_OK

- true_cluster_id: 5
- predicted_cluster_id: 5
- topk: 5

**log**
```
Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d
```

**top_matches**
- score=1.0000 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9836 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9836 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9709 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`
- score=0.9689 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`

**predicted_cluster_examples (head)**
- `Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- `Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056`

## #38 | TOP1_OK

- true_cluster_id: 5
- predicted_cluster_id: 5
- topk: 5

**log**
```
Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d
```

**top_matches**
- score=1.0000 tag=5:0 cid=5 text=`Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- score=0.9836 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9836 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`
- score=0.9709 tag=47:2 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/e741fef4-8974-43cf-9b11-6e6a9a08e0e0' before making global git config changes`
- score=0.9689 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`

**predicted_cluster_examples (head)**
- `Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d`
- `Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056`

## #39 | TOP1_OK

- true_cluster_id: 18
- predicted_cluster_id: 18
- topk: 5

**log**
```
Secret source: None
```

**top_matches**
- score=1.0000 tag=18:1 cid=18 text=`Secret source: None`
- score=0.8493 tag=18:0 cid=18 text=`Secret source: Actions`
- score=0.8417 tag=138:0 cid=138 text=`yarn install v1.22.22`
- score=0.8237 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.8236 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Secret source: Actions`
- `Secret source: None`

## #40 | TOP1_OK

- true_cluster_id: 18
- predicted_cluster_id: 18
- topk: 5

**log**
```
Secret source: None
```

**top_matches**
- score=1.0000 tag=18:1 cid=18 text=`Secret source: None`
- score=0.8493 tag=18:0 cid=18 text=`Secret source: Actions`
- score=0.8417 tag=138:0 cid=138 text=`yarn install v1.22.22`
- score=0.8237 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.8236 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Secret source: Actions`
- `Secret source: None`

## #41 | TOP1_OK

- true_cluster_id: 26
- predicted_cluster_id: 26
- topk: 5

**log**
```
ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9979 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9821 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9768 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=0.9768 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`

**predicted_cluster_examples (head)**
- `ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `ref: 71802995908aa85f00c80e117c635c5dbe28c45c`

## #42 | TOP1_OK

- true_cluster_id: 26
- predicted_cluster_id: 26
- topk: 5

**log**
```
ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9979 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9821 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9768 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=0.9768 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`

**predicted_cluster_examples (head)**
- `ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `ref: 71802995908aa85f00c80e117c635c5dbe28c45c`

## #43 | TOP1_OK

- true_cluster_id: 67
- predicted_cluster_id: 67
- topk: 5

**log**
```
[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
```

**top_matches**
- score=1.0000 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9848 tag=65:2 cid=65 text=`[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`
- score=0.9820 tag=65:0 cid=65 text=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9817 tag=65:1 cid=65 text=`[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- score=0.9807 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`
- `[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`

## #44 | TOP1_OK

- true_cluster_id: 67
- predicted_cluster_id: 67
- topk: 5

**log**
```
[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
```

**top_matches**
- score=1.0000 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9848 tag=65:2 cid=65 text=`[command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader`
- score=0.9820 tag=65:0 cid=65 text=`[command]/usr/bin/git config --local gc.auto 0`
- score=0.9817 tag=65:1 cid=65 text=`[command]/usr/bin/git config --local --unset-all extensions.worktreeConfig`
- score=0.9807 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`
- `[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`

## #45 | TOP1_OK

- true_cluster_id: 68
- predicted_cluster_id: 68
- topk: 5

**log**
```
[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
```

**top_matches**
- score=1.0000 tag=68:1 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.9826 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`
- score=0.9812 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9740 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9644 tag=67:0 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"`
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"`

## #46 | TOP1_OK

- true_cluster_id: 68
- predicted_cluster_id: 68
- topk: 5

**log**
```
[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
```

**top_matches**
- score=1.0000 tag=68:1 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --lo...`
- score=0.9826 tag=127:0 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-snapshot/node_modules/@babel/helpers: Cannot mkdir: No such file or...`
- score=0.9812 tag=127:2 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-config/node_modules/@babel/core/lib/tools: Cannot mkdir: No such fi...`
- score=0.9740 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9644 tag=67:0 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"`
- `[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"`

## #47 | TOP1_OK

- true_cluster_id: 71
- predicted_cluster_id: 71
- topk: 5

**base_log**
```
[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**mutated_log**
```
[command]/usr/bin_v2/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 9853fc208e384b34801168ab1fedb56c90448aab
```

**top_matches**
- score=0.9970 tag=71:1 cid=71 text=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`
- score=0.9953 tag=71:0 cid=71 text=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 71802995908aa85f00c80e117c635c5...`
- score=0.9328 tag=102:2 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/502712a1-1624-4483-ad36-5c994752e130 ...`
- score=0.9260 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9157 tag=102:0 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/a9aad03f-00b4-46e3-9e7a-338e0c8b4bc9 ...`

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
- score=1.0000 tag=71:1 cid=71 text=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4d...`
- score=0.9954 tag=71:0 cid=71 text=`[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 71802995908aa85f00c80e117c635c5...`
- score=0.9430 tag=47:0 cid=47 text=`Temporarily overriding HOME='/home/runner/work/_temp/6d67be73-ca0c-4978-b505-235131f88261' before making global git config changes`
- score=0.9351 tag=102:2 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/502712a1-1624-4483-ad36-5c994752e130 ...`
- score=0.9205 tag=115:1 cid=115 text=`Received 1274821257 of 1274821257 (100.0%), 152.5 MBs/sec`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin 71802995908aa85f00c80e117c635c5dbe28c45c`

## #49 | TOP1_OK

- true_cluster_id: 73
- predicted_cluster_id: 73
- topk: 5

**base_log**
```
* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD
```

**mutated_log**
```
* branch            07e437c198be972d1c15ad8f32ada4dfec4568a1 -> FETCH_HEAD
```

**top_matches**
- score=1.0000 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9979 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9825 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`
- score=0.9825 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=0.9825 tag=115:1 cid=115 text=`Received 1274821257 of 1274821257 (100.0%), 152.5 MBs/sec`

**predicted_cluster_examples (head)**
- `* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- `* branch            71802995908aa85f00c80e117c635c5dbe28c45c -> FETCH_HEAD`

## #50 | TOP1_OK

- true_cluster_id: 73
- predicted_cluster_id: 73
- topk: 5

**log**
```
* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD
```

**top_matches**
- score=1.0000 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- score=0.9979 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9825 tag=115:2 cid=115 text=`Received 398458880 of 470127531 (84.8%), 63.3 MBs/sec`
- score=0.9825 tag=115:0 cid=115 text=`Received 700448768 of 1274692111 (55.0%), 93.3 MBs/sec`
- score=0.9825 tag=115:1 cid=115 text=`Received 1274821257 of 1274821257 (100.0%), 152.5 MBs/sec`

**predicted_cluster_examples (head)**
- `* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`
- `* branch            71802995908aa85f00c80e117c635c5dbe28c45c -> FETCH_HEAD`

## #51 | TOP1_OK

- true_cluster_id: 77
- predicted_cluster_id: 77
- topk: 5

**log**
```
[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**top_matches**
- score=1.0000 tag=77:0 cid=77 text=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9877 tag=77:1 cid=77 text=`[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`
- score=0.9584 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9533 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`
- score=0.9525 tag=5:1 cid=5 text=`Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`

## #52 | TOP1_OK

- true_cluster_id: 77
- predicted_cluster_id: 77
- topk: 5

**base_log**
```
[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1
```

**mutated_log**
```
[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada1dfec3985a1
```

**top_matches**
- score=1.0000 tag=77:0 cid=77 text=`[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9877 tag=77:1 cid=77 text=`[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`
- score=0.9584 tag=67:1 cid=67 text=`[command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader`
- score=0.9533 tag=68:0 cid=68 text=`[command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extr...`
- score=0.9525 tag=5:1 cid=5 text=`Commit: cfce01a78eb650f23de9981e2e79cb8dc83e6056`

**predicted_cluster_examples (head)**
- `[command]/usr/bin/git checkout --progress --force 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- `[command]/usr/bin/git checkout --progress --force 71802995908aa85f00c80e117c635c5dbe28c45c`

## #53 | TOP1_OK

- true_cluster_id: 78
- predicted_cluster_id: 78
- topk: 5

**base_log**
```
Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.
```

**mutated_log**
```
Error: Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.
```

**top_matches**
- score=0.9996 tag=78:0 cid=78 text=`Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`
- score=0.9864 tag=78:1 cid=78 text=`Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- score=0.9125 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9114 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9037 tag=73:0 cid=73 text=`* branch            07e437c198be972d7c15ad8f32ada4dfec3985a1 -> FETCH_HEAD`

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
- score=1.0000 tag=78:0 cid=78 text=`Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`
- score=0.9874 tag=78:1 cid=78 text=`Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- score=0.9076 tag=22:0 cid=22 text=`Download action repository 'actions/cache@v4' (SHA:0400d5f644dc74513175e3cd8d07132dd4860809)`
- score=0.9074 tag=26:1 cid=26 text=`ref: 07e437c198be972d7c15ad8f32ada4dfec3985a1`
- score=0.9029 tag=22:2 cid=22 text=`Download action repository 'actions/checkout@v4' (SHA:08eba0b27e820071cde6df949e0beb9ba4906955)`

**predicted_cluster_examples (head)**
- `Note: switching to '07e437c198be972d7c15ad8f32ada4dfec3985a1'.`
- `Note: switching to '71802995908aa85f00c80e117c635c5dbe28c45c'.`

## #55 | TOP1_OK

- true_cluster_id: 114
- predicted_cluster_id: 114
- topk: 5

**log**
```
Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**top_matches**
- score=1.0000 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9998 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`
- score=0.9772 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9734 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9691 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #56 | TOP1_OK

- true_cluster_id: 114
- predicted_cluster_id: 114
- topk: 5

**base_log**
```
Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**mutated_log**
```
Error: Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**top_matches**
- score=0.9999 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9997 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`
- score=0.9766 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9719 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9682 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Cache hit for: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #57 | TOP1_OK

- true_cluster_id: 119
- predicted_cluster_id: 119
- topk: 5

**log**
```
Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**top_matches**
- score=1.0000 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`
- score=0.9998 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9803 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9764 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9728 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #58 | TOP1_OK

- true_cluster_id: 119
- predicted_cluster_id: 119
- topk: 5

**log**
```
Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f
```

**top_matches**
- score=1.0000 tag=119:1 cid=119 text=`Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3...`
- score=0.9998 tag=114:0 cid=114 text=`Cache hit for: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`
- score=0.9803 tag=128:0 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@typescript-eslint/typescript-estree/dist/use-at-your-own-risk.js: Canno...`
- score=0.9764 tag=128:2 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/jest-circus/node_modules/@sinclair/typebox/value/pointer.d.ts: Cannot ha...`
- score=0.9728 tag=128:1 cid=128 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@jest/core/build/version.js: Cannot hard link to ‘compiler/node_modules/...`

**predicted_cluster_examples (head)**
- `Cache restored from key: node-cache-Linux-x64-yarn-8f02efa48a3cd46b43e33a57ee18484c35a2de8773628cd71b2f773158751dd4`
- `Cache saved with key: runtime-and-compiler-eslint_e2e-node_modules-v6-X64-Linux-9dea77b537696b6bc8e5947b26f62d36179dab5fd167a78d3585b024d0d3550f`

## #59 | TOP1_OK

- true_cluster_id: 138
- predicted_cluster_id: 138
- topk: 5

**log**
```
yarn install v1.22.22
```

**top_matches**
- score=1.0000 tag=138:0 cid=138 text=`yarn install v1.22.22`
- score=0.9689 tag=138:1 cid=138 text=`yarn run v1.22.22`
- score=0.9302 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9296 tag=102:1 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f ...`
- score=0.9256 tag=102:0 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/a9aad03f-00b4-46e3-9e7a-338e0c8b4bc9 ...`

**predicted_cluster_examples (head)**
- `yarn install v1.22.22`
- `yarn run v1.22.22`

## #60 | TOP1_OK

- true_cluster_id: 138
- predicted_cluster_id: 138
- topk: 5

**log**
```
yarn install v1.22.22
```

**top_matches**
- score=1.0000 tag=138:0 cid=138 text=`yarn install v1.22.22`
- score=0.9689 tag=138:1 cid=138 text=`yarn run v1.22.22`
- score=0.9302 tag=127:1 cid=127 text=`/usr/bin/tar: node_modules/babel-plugin-react-compiler/node_modules/@babel/traverse/lib: Cannot mkdir: No such file or directory`
- score=0.9296 tag=102:1 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/6f1f3bb6-b439-4a0f-b78f-e54fd5c3bd9f ...`
- score=0.9256 tag=102:0 cid=102 text=`[command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/a9aad03f-00b4-46e3-9e7a-338e0c8b4bc9 ...`

**predicted_cluster_examples (head)**
- `yarn install v1.22.22`
- `yarn run v1.22.22`
