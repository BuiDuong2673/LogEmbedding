# Test Log Report: d2klab_robustness_mode-examples_seed0.jsonl

- total: 20
- correct: 19
- no_match: 1
- accuracy: 0.9500

### #1 | OK

- true_cluster_id: 191
- predicted_cluster_id: 191
- confidence: 1.0
- true_template: `x ./hdf5-1.14.1-2/`
- matched_template: `x ./hdf5-1.14.1-2/`

**base_log**
```
x ./hdf5-1.14.1-2/tools/test/h5format_convert/testfiles/h5fc_nonexistdset_file.ddl.err
```

**mutated_log**
```
x ./hdf5-1.14.2-2/tools/test/h5format_convert/testfiles/h5fc_nonexistdset_file.ddl.err
```

**predicted_cluster_examples (head)**
- `x ./hdf5-1.14.1-2/`
- `x ./hdf5-1.14.1-2/.autom4te.cfg`

### #2 | OK

- true_cluster_id: 191
- predicted_cluster_id: 191
- confidence: 1.0
- true_template: `x ./hdf5-1.14.1-2/`
- matched_template: `x ./hdf5-1.14.1-2/`

**log**
```
x ./hdf5-1.14.1-2/tools/test/h5format_convert/testfiles/h5fc_nonexistdset_file.ddl.err
```

**predicted_cluster_examples (head)**
- `x ./hdf5-1.14.1-2/`
- `x ./hdf5-1.14.1-2/.autom4te.cfg`

### #3 | OK

- true_cluster_id: 640
- predicted_cluster_id: 640
- confidence: 1.0
- true_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- matched_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

**log**
```
copying tables/tests/elink.h5 -> build/lib.macosx-10.9-x86_64-cpython-311/tables/tests
```

**predicted_cluster_examples (head)**
- `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- `copying tables/description.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

### #4 | OK

- true_cluster_id: 640
- predicted_cluster_id: 640
- confidence: 1.0
- true_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- matched_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

**base_log**
```
copying tables/tests/elink.h5 -> build/lib.macosx-10.9-x86_64-cpython-311/tables/tests
```

**mutated_log**
```
copying tables/tests/elink.h9 -> build/lib.macosx-10.9-x86_24-cpython-311/tables/tests
```

**predicted_cluster_examples (head)**
- `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- `copying tables/description.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

### #5 | OK

- true_cluster_id: 365
- predicted_cluster_id: 365
- confidence: 1.0
- true_template: `CC H5detect.o`
- matched_template: `CC H5detect.o`

**log**
```
CC       H5UC.lo
```

**predicted_cluster_examples (head)**
- `CC       H5detect.o`
- `CC       H5make_libsettings.o`

### #6 | OK

- true_cluster_id: 365
- predicted_cluster_id: 365
- confidence: 1.0
- true_template: `CC H5detect.o`
- matched_template: `CC H5detect.o`

**base_log**
```
CC       H5UC.lo
```

**mutated_log**
```
CC       H1UC.lo
```

**predicted_cluster_examples (head)**
- `CC       H5detect.o`
- `CC       H5make_libsettings.o`

### #7 | OK

- true_cluster_id: 459
- predicted_cluster_id: 459
- confidence: 1.0
- true_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- matched_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`

**log**
```
Receiving objects:  68% (24647/36245), 9.98 MiB | 19.96 MiB/s
```

**predicted_cluster_examples (head)**
- `Receiving objects:  31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- `Receiving objects:  32% (11599/36245), 9.98 MiB | 19.96 MiB/s`

### #8 | OK

- true_cluster_id: 459
- predicted_cluster_id: 459
- confidence: 1.0
- true_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- matched_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`

**base_log**
```
Receiving objects:  68% (24647/36245), 9.98 MiB | 19.96 MiB/s
```

**mutated_log**
```
Receiving objects:  68% (24647/36245), 9.98 MiB | 19.97 MiB/s
```

**predicted_cluster_examples (head)**
- `Receiving objects:  31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- `Receiving objects:  32% (11599/36245), 9.98 MiB | 19.96 MiB/s`

### #9 | OK

- true_cluster_id: 642
- predicted_cluster_id: 642
- confidence: 1.0
- true_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**base_log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/usr/local/include -I/usr/include -Ic-blosc/internal-complibs/zstd-1.5.5 -I/include -Ic-blosc/internal-complibs/lz4-1.9.4 -I/opt/local/include -I/sw/include -Ic-blosc/blosc -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/include -Ihdf5-blosc/src -I/opt/include -Ihdf5-blosc2/src -Ic-blosc/internal-complibs/zlib-1.2.13 -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/lib/python3.9/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp39-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9 -c src/typeconv.c -o build/temp.macosx-10.9-x86_64-cpython-39/src/typeconv.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

**mutated_log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/usr/local/include -I/usr/include -Ic-blosc/internal-complibs/zstd-1.5.5 -I/include -Ic-blosc/internal-complibs/lz4-1.9.4-x86_64 -I/opt/local/include -I/sw/include -Ic-blosc/blosc -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/include -Ihdf5-blosc/src -I/opt/include -Ihdf5-blosc2/src -Ic-blosc/internal-complibs/zlib-1.2.13 -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/lib/python3.9/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp39-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9 -c src/typeconv.c -o build/temp.macosx-10.9-x86_64-cpython-39/src/typeconv.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

**predicted_cluster_examples (head)**
- `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-sse2.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-sse2.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

### #10 | OK

- true_cluster_id: 642
- predicted_cluster_id: 642
- confidence: 1.0
- true_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**base_log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/usr/local/include -I/usr/include -Ic-blosc/internal-complibs/zstd-1.5.5 -I/include -Ic-blosc/internal-complibs/lz4-1.9.4 -I/opt/local/include -I/sw/include -Ic-blosc/blosc -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/include -Ihdf5-blosc/src -I/opt/include -Ihdf5-blosc2/src -Ic-blosc/internal-complibs/zlib-1.2.13 -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/lib/python3.9/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp39-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9 -c src/typeconv.c -o build/temp.macosx-10.9-x86_64-cpython-39/src/typeconv.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

**mutated_log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/usr/local/include -I/usr/include -Ic-blosc/internal-complibs/zstd-1.5.5 -I/include -Ic-blosc/internal-complibs/lz4-1.9.4 -I/opt/local/include -I/sw/include -Ic-blosc/blosc -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/include -Ihdf5-blosc/src -I/opt-x86_64/include -Ihdf5-blosc2/src -Ic-blosc/internal-complibs/zlib-1.2.13 -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/lib/python3.9/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp39-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/2.9/include/python3.9 -c src/typeconv.c -o build/temp.macosx-10.9-x86_64-cpython-39/src/typeconv.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

**predicted_cluster_examples (head)**
- `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-sse2.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-sse2.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

### #11 | WRONG

- true_cluster_id: 95
- predicted_cluster_id: -1
- confidence: 0.0
- true_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- matched_template: `No match`

**base_log**
```
[ 83%] Building C object programs/CMakeFiles/zstd.dir/tmp/zstd-1.5.2/programs/zstdcli_trace.c.o
```

**mutated_log**
```
Error: [ 83%] Building C object programs/CMakeFiles/zstd.dir/tmp/zstd-1.5.2/programs/zstdcli_trace.c.o_v2
```

### #12 | OK

- true_cluster_id: 95
- predicted_cluster_id: 95
- confidence: 1.0
- true_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- matched_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`

**base_log**
```
[ 83%] Building C object programs/CMakeFiles/zstd.dir/tmp/zstd-1.5.2/programs/zstdcli_trace.c.o
```

**mutated_log**
```
[ 83%] Building C object programs/CMakeFiles/zstd.dir/tmp/zstd-3.5.2/programs/zstdcli_trace.c.o
```

**predicted_cluster_examples (head)**
- `[  1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- `[  2%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1_99.c.o`

### #13 | OK

- true_cluster_id: 658
- predicted_cluster_id: 658
- confidence: 1.0
- true_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- matched_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`

**log**
```
tables/indexesextension.c:30326:3: warning: code will never be executed [-Wunreachable-code]
```

**predicted_cluster_examples (head)**
- `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:376:9: warning: code will never be executed [-Wunreachable-code]`

### #14 | OK

- true_cluster_id: 658
- predicted_cluster_id: 658
- confidence: 1.0
- true_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- matched_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`

**log**
```
tables/indexesextension.c:30326:3: warning: code will never be executed [-Wunreachable-code]
```

**predicted_cluster_examples (head)**
- `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:376:9: warning: code will never be executed [-Wunreachable-code]`

### #15 | OK

- true_cluster_id: 132
- predicted_cluster_id: 132
- confidence: 1.0
- true_template: `creating pkgconfig`
- matched_template: `creating pkgconfig`

**log**
```
creating build/temp.macosx-10.9-x86_64-cpython-310/c-blosc/internal-complibs
```

**predicted_cluster_examples (head)**
- `creating pkgconfig`
- `creating src/H5pubconf.h`

### #16 | OK

- true_cluster_id: 132
- predicted_cluster_id: 132
- confidence: 1.0
- true_template: `creating pkgconfig`
- matched_template: `creating pkgconfig`

**base_log**
```
creating build/temp.macosx-10.9-x86_64-cpython-310/c-blosc/internal-complibs
```

**mutated_log**
```
creating build/temp.macosx-12.11-x86_64-cpython-310/c-blosc/internal-complibs
```

**predicted_cluster_examples (head)**
- `creating pkgconfig`
- `creating src/H5pubconf.h`

### #17 | OK

- true_cluster_id: 456
- predicted_cluster_id: 456
- confidence: 1.0
- true_template: `remote: Enumerating objects: 36245, done.`
- matched_template: `remote: Enumerating objects: 36245, done.`

**log**
```
remote: Compressing objects:  38% (120/314)
```

**predicted_cluster_examples (head)**
- `remote: Enumerating objects: 36245, done.`
- `remote: Counting objects:   0% (1/974)`

### #18 | OK

- true_cluster_id: 456
- predicted_cluster_id: 456
- confidence: 1.0
- true_template: `remote: Enumerating objects: 36245, done.`
- matched_template: `remote: Enumerating objects: 36245, done.`

**log**
```
remote: Compressing objects:  38% (120/314)
```

**predicted_cluster_examples (head)**
- `remote: Enumerating objects: 36245, done.`
- `remote: Counting objects:   0% (1/974)`

### #19 | OK

- true_cluster_id: 366
- predicted_cluster_id: 366
- confidence: 1.0
- true_template: `CCLD H5detect`
- matched_template: `CCLD H5detect`

**log**
```
CCLD     h5repackgentest
```

**predicted_cluster_examples (head)**
- `CCLD     H5detect`
- `CCLD     H5make_libsettings`

### #20 | OK

- true_cluster_id: 366
- predicted_cluster_id: 366
- confidence: 1.0
- true_template: `CCLD H5detect`
- matched_template: `CCLD H5detect`

**base_log**
```
CCLD     h5repackgentest
```

**mutated_log**
```
CCLD     h0repackgentest
```

**predicted_cluster_examples (head)**
- `CCLD     H5detect`
- `CCLD     H5make_libsettings`
