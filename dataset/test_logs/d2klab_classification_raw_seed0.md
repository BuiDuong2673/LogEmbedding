# Test Log Report: d2klab_classification_raw_seed0.jsonl

- total: 80
- correct: 78
- no_match: 2
- accuracy: 0.9750

### #1

- true_cluster_id: 191
- predicted_cluster_id: 191
- confidence: 1.0
- true_template: `x ./hdf5-1.14.1-2/`
- matched_template: `x ./hdf5-1.14.1-2/`

**log**
```
x ./hdf5-1.14.1-2/tools/test/h5format_convert/testfiles/h5fc_nonexistdset_file.ddl.err
```

### #2

- true_cluster_id: 191
- predicted_cluster_id: 191
- confidence: 1.0
- true_template: `x ./hdf5-1.14.1-2/`
- matched_template: `x ./hdf5-1.14.1-2/`

**log**
```
x ./hdf5-1.14.1-2/tools/test/h5stat/testfiles/h5stat_newgrat-UA.ddl
```

### #3

- true_cluster_id: 191
- predicted_cluster_id: 191
- confidence: 1.0
- true_template: `x ./hdf5-1.14.1-2/`
- matched_template: `x ./hdf5-1.14.1-2/`

**log**
```
x ./hdf5-1.14.1-2/config/gnu-warnings/gfort-general
```

### #4

- true_cluster_id: 640
- predicted_cluster_id: 640
- confidence: 1.0
- true_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- matched_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

**log**
```
copying build/lib.macosx-10.9-x86_64-cpython-39/tables/tests/test_tablesMD.py -> build/bdist.macosx-10.9-x86_64/wheel/tables/tests
```

### #5

- true_cluster_id: 640
- predicted_cluster_id: 640
- confidence: 1.0
- true_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- matched_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

**log**
```
copying build/lib.macosx-10.9-x86_64-cpython-311/tables/tests/test_ref_array1.mat -> build/bdist.macosx-10.9-x86_64/wheel/tables/tests
```

### #6

- true_cluster_id: 640
- predicted_cluster_id: 640
- confidence: 1.0
- true_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`
- matched_template: `copying tables/link.py -> build/lib.macosx-10.9-x86_64-cpython-38/tables`

**log**
```
copying tables/tests/slink.h5 -> build/lib.macosx-10.9-x86_64-cpython-311/tables/tests
```

### #7

- true_cluster_id: 365
- predicted_cluster_id: 365
- confidence: 1.0
- true_template: `CC H5detect.o`
- matched_template: `CC H5detect.o`

**log**
```
CC       ttsafe_attr_vlen.o
```

### #8

- true_cluster_id: 365
- predicted_cluster_id: 365
- confidence: 1.0
- true_template: `CC H5detect.o`
- matched_template: `CC H5detect.o`

**log**
```
CC       H5VLnative_introspect.lo
```

### #9

- true_cluster_id: 365
- predicted_cluster_id: 365
- confidence: 1.0
- true_template: `CC H5detect.o`
- matched_template: `CC H5detect.o`

**log**
```
CC       h5diff_common.o
```

### #10

- true_cluster_id: 459
- predicted_cluster_id: 459
- confidence: 1.0
- true_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- matched_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`

**log**
```
Receiving objects:  56% (20298/36245), 15.75 MiB | 10.39 MiB/s
```

### #11

- true_cluster_id: 459
- predicted_cluster_id: 459
- confidence: 1.0
- true_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- matched_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`

**log**
```
Receiving objects: 100% (36245/36245), 29.80 MiB | 29.80 MiB/s
```

### #12

- true_cluster_id: 459
- predicted_cluster_id: 459
- confidence: 1.0
- true_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`
- matched_template: `Receiving objects: 31% (11236/36245), 9.98 MiB | 19.96 MiB/s`

**log**
```
Receiving objects:  69% (25010/36245), 9.52 MiB | 18.49 MiB/s
```

### #13

- true_cluster_id: 642
- predicted_cluster_id: 642
- confidence: 1.0
- true_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/usr/local/include -I/usr/include -Ic-blosc/internal-complibs/zstd-1.5.5 -I/include -Ic-blosc/internal-complibs/lz4-1.9.4 -I/opt/local/include -I/sw/include -Ic-blosc/blosc -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/include -Ihdf5-blosc/src -I/opt/include -Ihdf5-blosc2/src -Ic-blosc/internal-complibs/zlib-1.2.13 -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-4quz3d7b/overlay/lib/python3.9/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp39-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9 -c c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c -o build/temp.macosx-10.9-x86_64-cpython-39/c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #14

- true_cluster_id: 642
- predicted_cluster_id: 642
- confidence: 1.0
- true_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/internal-complibs/zstd-1.5.5/compress/huf_compress.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/internal-complibs/zstd-1.5.5/compress/huf_compress.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #15

- true_cluster_id: 642
- predicted_cluster_id: 642
- confidence: 1.0
- true_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-38/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ihdf5-blosc/src -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/include -I/opt/include -Ic-blosc/internal-complibs/lz4-1.9.4 -Ihdf5-blosc2/src -I/usr/include -I/tmp/hdf5/include -I/usr/local/include -I/opt/local/include -I/include -I/sw/include -Ic-blosc/internal-complibs/zstd-1.5.5/common -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-eoo4gzd4/overlay/lib/python3.8/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp38-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -c src/typeconv.c -o build/temp.macosx-10.9-x86_64-cpython-38/src/typeconv.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #16

- true_cluster_id: 95
- predicted_cluster_id: 95
- confidence: 1.0
- true_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- matched_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`

**log**
```
[ 24%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1c_xx.c.o
```

### #17

- true_cluster_id: 95
- predicted_cluster_id: 95
- confidence: 1.0
- true_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- matched_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`

**log**
```
[ 61%] Building C object lib/CMakeFiles/libzstd_static.dir/tmp/zstd-1.5.2/lib/compress/zstdmt_compress.c.o
```

### #18

- true_cluster_id: 95
- predicted_cluster_id: 95
- confidence: 1.0
- true_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`
- matched_template: `[ 1%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1.c.o`

**log**
```
[ 17%] Building C object CMakeFiles/lzo_static_lib.dir/src/lzo1c_5.c.o
```

### #19

- true_cluster_id: 658
- predicted_cluster_id: 658
- confidence: 1.0
- true_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- matched_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`

**log**
```
tables/lrucacheextension.c:8485:3: warning: code will never be executed [-Wunreachable-code]
```

### #20

- true_cluster_id: 658
- predicted_cluster_id: 658
- confidence: 1.0
- true_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- matched_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`

**log**
```
tables/indexesextension.c:30091:3: warning: code will never be executed [-Wunreachable-code]
```

### #21

- true_cluster_id: 658
- predicted_cluster_id: 658
- confidence: 1.0
- true_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`
- matched_template: `c-blosc/internal-complibs/zstd-1.5.5/compress/zstdmt_compress.c:112:9: warning: code will never be executed [-Wunreachable-code]`

**log**
```
tables/hdf5extension.c:21706:3: warning: code will never be executed [-Wunreachable-code]
```

### #22

- true_cluster_id: 132
- predicted_cluster_id: 132
- confidence: 1.0
- true_template: `creating pkgconfig`
- matched_template: `creating pkgconfig`

**log**
```
creating tables-3.8.1.dev0/c-blosc/internal-complibs/zlib-1.2.13/contrib/infback9
```

### #23

- true_cluster_id: 132
- predicted_cluster_id: 132
- confidence: 1.0
- true_template: `creating pkgconfig`
- matched_template: `creating pkgconfig`

**log**
```
creating build/lib.linux-x86_64-cpython-311
```

### #24

- true_cluster_id: 132
- predicted_cluster_id: 132
- confidence: 1.0
- true_template: `creating pkgconfig`
- matched_template: `creating pkgconfig`

**log**
```
creating tables-3.8.1.dev0/doc
```

### #25

- true_cluster_id: 456
- predicted_cluster_id: 456
- confidence: 1.0
- true_template: `remote: Enumerating objects: 36245, done.`
- matched_template: `remote: Enumerating objects: 36245, done.`

**log**
```
remote: Counting objects:  36% (351/974)
```

### #26

- true_cluster_id: 456
- predicted_cluster_id: 456
- confidence: 1.0
- true_template: `remote: Enumerating objects: 36245, done.`
- matched_template: `remote: Enumerating objects: 36245, done.`

**log**
```
remote: Counting objects:  78% (760/974)
```

### #27

- true_cluster_id: 456
- predicted_cluster_id: 456
- confidence: 1.0
- true_template: `remote: Enumerating objects: 36245, done.`
- matched_template: `remote: Enumerating objects: 36245, done.`

**log**
```
remote: Counting objects:  24% (234/974)
```

### #28

- true_cluster_id: 366
- predicted_cluster_id: 366
- confidence: 1.0
- true_template: `CCLD H5detect`
- matched_template: `CCLD H5detect`

**log**
```
CCLD     gheap
```

### #29

- true_cluster_id: 366
- predicted_cluster_id: 366
- confidence: 1.0
- true_template: `CCLD H5detect`
- matched_template: `CCLD H5detect`

**log**
```
CCLD     test_ld
```

### #30

- true_cluster_id: 366
- predicted_cluster_id: 366
- confidence: 1.0
- true_template: `CCLD H5detect`
- matched_template: `CCLD H5detect`

**log**
```
CCLD     tcheck_version
```

### #31

- true_cluster_id: 693
- predicted_cluster_id: 693
- confidence: 1.0
- true_template: `adding 'tables/__init__.py'`
- matched_template: `adding 'tables/__init__.py'`

**log**
```
adding 'tables/tests/test_expression.py'
```

### #32

- true_cluster_id: 693
- predicted_cluster_id: 693
- confidence: 1.0
- true_template: `adding 'tables/__init__.py'`
- matched_template: `adding 'tables/__init__.py'`

**log**
```
adding 'tables/tests/test_vlarray.py'
```

### #33

- true_cluster_id: 693
- predicted_cluster_id: 693
- confidence: 1.0
- true_template: `adding 'tables/__init__.py'`
- matched_template: `adding 'tables/__init__.py'`

**log**
```
adding 'tables/indexes.py'
```

### #34

- true_cluster_id: 409
- predicted_cluster_id: 409
- confidence: 1.0
- true_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`
- matched_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`

**log**
```
Downloading Cython-3.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.1 kB)
```

### #35

- true_cluster_id: 409
- predicted_cluster_id: 409
- confidence: 1.0
- true_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`
- matched_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`

**log**
```
Downloading msgpack-1.0.6-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (525 kB)
```

### #36

- true_cluster_id: 409
- predicted_cluster_id: 409
- confidence: 1.0
- true_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`
- matched_template: `Downloading cibuildwheel-2.16.0-py3-none-any.whl.metadata (22 kB)`

**log**
```
Downloading Cython-3.0.2-cp311-cp311-win_amd64.whl.metadata (3.2 kB)
```

### #37

- true_cluster_id: 290
- predicted_cluster_id: 290
- confidence: 1.0
- true_template: `config.status: creating src/libhdf5.settings`
- matched_template: `config.status: creating src/libhdf5.settings`

**log**
```
config.status: creating tools/test/h5ls/testh5ls.sh
```

### #38

- true_cluster_id: 290
- predicted_cluster_id: 290
- confidence: 1.0
- true_template: `config.status: creating src/libhdf5.settings`
- matched_template: `config.status: creating src/libhdf5.settings`

**log**
```
config.status: creating hl/tools/h5watch/Makefile
```

### #39

- true_cluster_id: 290
- predicted_cluster_id: 290
- confidence: 1.0
- true_template: `config.status: creating src/libhdf5.settings`
- matched_template: `config.status: creating src/libhdf5.settings`

**log**
```
config.status: creating java/examples/groups/Makefile
```

### #40

- true_cluster_id: 411
- predicted_cluster_id: 411
- confidence: 1.0
- true_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`
- matched_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`

**log**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 57.3 MB/s eta 0:00:00
```

### #41

- true_cluster_id: 411
- predicted_cluster_id: 411
- confidence: 1.0
- true_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`
- matched_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`

**log**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 42.0 MB/s eta 0:00:00
```

### #42

- true_cluster_id: 411
- predicted_cluster_id: 411
- confidence: 1.0
- true_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`
- matched_template: `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 kB 5.7 MB/s eta 0:00:00`

**log**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 44.2 MB/s eta 0:00:00
```

### #43

- true_cluster_id: 392
- predicted_cluster_id: 392
- confidence: 1.0
- true_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`
- matched_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`

**log**
```
+ /usr/bin/install -c ./h5_extlink.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.
```

### #44

- true_cluster_id: 392
- predicted_cluster_id: 392
- confidence: 1.0
- true_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`
- matched_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`

**log**
```
+ /usr/bin/install -c ./h5_vds-percival.c /io/hdf5_build/share/hdf5_examples/c/.
```

### #45

- true_cluster_id: 392
- predicted_cluster_id: 392
- confidence: 1.0
- true_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`
- matched_template: `+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.`

**log**
```
+ /usr/bin/install -c ./h5_write.c /Users/runner/work/PyTables/PyTables/hdf5_build/share/hdf5_examples/c/.
```

### #46

- true_cluster_id: 462
- predicted_cluster_id: 462
- confidence: 1.0
- true_template: `Resolving deltas: 0% (0/28232)`
- matched_template: `Resolving deltas: 0% (0/28232)`

**log**
```
Resolving deltas:  77% (21739/28232)
```

### #47

- true_cluster_id: 462
- predicted_cluster_id: 462
- confidence: 1.0
- true_template: `Resolving deltas: 0% (0/28232)`
- matched_template: `Resolving deltas: 0% (0/28232)`

**log**
```
Resolving deltas:  62% (17504/28232)
```

### #48

- true_cluster_id: 462
- predicted_cluster_id: 462
- confidence: 1.0
- true_template: `Resolving deltas: 0% (0/28232)`
- matched_template: `Resolving deltas: 0% (0/28232)`

**log**
```
Resolving deltas:  61% (17222/28232)
```

### #49

- true_cluster_id: 408
- predicted_cluster_id: 408
- confidence: 1.0
- true_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`
- matched_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`

**log**
```
Obtaining dependency information for jaraco.classes from https://files.pythonhosted.org/packages/c7/6b/1bc8fa93ea85146e08f0e0883bc579b7c7328364ed7df90b1628dcb36e10/jaraco.classes-3.3.0-py3-none-any.whl.metadata
```

### #50

- true_cluster_id: 408
- predicted_cluster_id: 408
- confidence: 1.0
- true_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`
- matched_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`

**log**
```
Obtaining dependency information for numexpr>=2.6.2 from https://files.pythonhosted.org/packages/6a/5b/4e36b82a51e261d24240e113abc8567e283ccd41d07d2e4b58b19438bf25/numexpr-2.8.6-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata
```

### #51

- true_cluster_id: 408
- predicted_cluster_id: 408
- confidence: 1.0
- true_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`
- matched_template: `Obtaining dependency information for cibuildwheel from https://files.pythonhosted.org/packages/a6/d3/6882ec437b47e7e5aca04ad1c604e06ee1c0a1c5ab0c4bebc25cfd93a4fa/cibuildwheel-2.16.0-py3-none-any.whl.metadata`

**log**
```
Obtaining dependency information for cython>=0.29.32 from https://files.pythonhosted.org/packages/e2/18/ba1a01c0ed30b248878b98fcf0654141c1c0e476166b5dcb4d7c04214884/Cython-3.0.2-cp311-cp311-macosx_10_9_x86_64.whl.metadata
```

### #52 | NO_MATCH

- true_cluster_id: 6094
- predicted_cluster_id: -1
- confidence: 0.0
- true_template: `ssdescr' on page 90 undefined on input line 7705.`
- matched_template: `No match`

**log**
```
le.read_where' on page 213 undefined on input line 19271.
```

### #53

- true_cluster_id: 6094
- predicted_cluster_id: 6094
- confidence: 1.0
- true_template: `ssdescr' on page 90 undefined on input line 7705.`
- matched_template: `ssdescr' on page 90 undefined on input line 7705.`

**log**
```
umn.create_index' on page 114 undefined on input line 10682.
```

### #54 | NO_MATCH

- true_cluster_id: 6094
- predicted_cluster_id: -1
- confidence: 0.0
- true_template: `ssdescr' on page 90 undefined on input line 7705.`
- matched_template: `No match`

**log**
```
DE_CACHE_SLOTS' on page 203 undefined on input line 18325.
```

### #55

- true_cluster_id: 538
- predicted_cluster_id: 538
- confidence: 1.0
- true_template: `[32m✓ [0m0.19s`
- matched_template: `[32m✓ [0m0.19s`

**log**
```
[32m✓ [0m11.76s
```

### #56

- true_cluster_id: 538
- predicted_cluster_id: 538
- confidence: 1.0
- true_template: `[32m✓ [0m0.19s`
- matched_template: `[32m✓ [0m0.19s`

**log**
```
[32m✓ [0m42.04s
```

### #57

- true_cluster_id: 538
- predicted_cluster_id: 538
- confidence: 1.0
- true_template: `[32m✓ [0m0.19s`
- matched_template: `[32m✓ [0m0.19s`

**log**
```
[32m✓ [0m64.00s
```

### #58

- true_cluster_id: 197
- predicted_cluster_id: 197
- confidence: 1.0
- true_template: `checking for gawk... no`
- matched_template: `checking for gawk... no`

**log**
```
checking for otool64... no
```

### #59

- true_cluster_id: 197
- predicted_cluster_id: 197
- confidence: 1.0
- true_template: `checking for gawk... no`
- matched_template: `checking for gawk... no`

**log**
```
checking for objdir... .libs
```

### #60

- true_cluster_id: 197
- predicted_cluster_id: 197
- confidence: 1.0
- true_template: `checking for gawk... no`
- matched_template: `checking for gawk... no`

**log**
```
checking for objdump... objdump
```

### #61

- true_cluster_id: 5738
- predicted_cluster_id: 5738
- confidence: 1.0
- true_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`
- matched_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`

**log**
```
gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c src/H5ATTR.c -o build/temp.linux-x86_64-cpython-311/src/H5ATTR.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2
```

### #62

- true_cluster_id: 5738
- predicted_cluster_id: 5738
- confidence: 1.0
- true_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`
- matched_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`

**log**
```
gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/internal-complibs/zstd-1.5.5/dictBuilder/fastcover.c -o build/temp.linux-x86_64-cpython-311/c-blosc/internal-complibs/zstd-1.5.5/dictBuilder/fastcover.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2
```

### #63

- true_cluster_id: 5738
- predicted_cluster_id: 5738
- confidence: 1.0
- true_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`
- matched_template: `gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/blosc/bitshuffle-avx2.c -o build/temp.linux-x86_64-cpython-311/c-blosc/blosc/bitshuffle-avx2.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2`

**log**
```
gcc -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -I/usr/include/hdf5/serial -Ihdf5-blosc/src -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/blosc -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc2/src -I/opt/hostedtoolcache/Python/3.11.5/x64/include -I/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/numpy/core/include -I/opt/hostedtoolcache/Python/3.11.5/x64/include/python3.11 -c c-blosc/internal-complibs/lz4-1.9.4/lz4hc.c -o build/temp.linux-x86_64-cpython-311/c-blosc/internal-complibs/lz4-1.9.4/lz4hc.o -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2 -DSHUFFLE_AVX2_ENABLED -mavx2
```

### #64

- true_cluster_id: 5957
- predicted_cluster_id: 5957
- confidence: 1.0
- true_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`
- matched_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`

**log**
```
LaTeX Warning: Hyper reference `usersguide/libref/file_class:tables.File.list_n
```

### #65

- true_cluster_id: 5957
- predicted_cluster_id: 5957
- confidence: 1.0
- true_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`
- matched_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`

**log**
```
LaTeX Warning: Hyper reference `usersguide/libref/link_classes:softlinkclassdes
```

### #66

- true_cluster_id: 5957
- predicted_cluster_id: 5957
- confidence: 1.0
- true_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`
- matched_template: `LaTeX Warning: Hyper reference `usersguide/libref/helper_classes:unimplementedc`

**log**
```
LaTeX Warning: Hyper reference `usersguide/libref/structured_storage:tablemetho
```

### #67

- true_cluster_id: 725
- predicted_cluster_id: 725
- confidence: 1.0
- true_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/internal-complibs/zstd-1.5.5/legacy/zstd_v06.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/internal-complibs/zstd-1.5.5/legacy/zstd_v06.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #68

- true_cluster_id: 725
- predicted_cluster_id: 725
- confidence: 1.0
- true_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/internal-complibs/zlib-1.2.13/deflate.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/internal-complibs/zlib-1.2.13/deflate.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #69

- true_cluster_id: 725
- predicted_cluster_id: 725
- confidence: 1.0
- true_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`
- matched_template: `/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/blosc/bitshuffle-generic.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/blosc/bitshuffle-generic.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2`

**log**
```
/usr/bin/clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -g -g0 -arch x86_64 -DNDEBUG=1 -DHAVE_LZO2_LIB=1 -DHAVE_BZ2_LIB=1 -DHAVE_BLOSC2_LIB=1 -DHAVE_LZ4=1 -DHAVE_ZLIB=1 -DHAVE_ZSTD=1 -DZSTD_DISABLE_ASM=1 -Ihdf5-blosc2/src -I/opt/local/include -I/sw/include -I/include -Ic-blosc/internal-complibs/zlib-1.2.13 -Ic-blosc/internal-complibs/zstd-1.5.5 -Ic-blosc/internal-complibs/lz4-1.9.4 -Ic-blosc/internal-complibs/zstd-1.5.5/common -Ihdf5-blosc/src -I/usr/include -I/usr/local/include -Ic-blosc/blosc -I/opt/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/include -I/tmp/hdf5/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/pip-build-env-fbisbv89/overlay/lib/python3.11/site-packages/numpy/core/include -I/private/var/folders/24/8k48jl6d249_n_qfxwsl6xvm0000gn/T/cibw-run-vrmm71ck/cp311-macosx_x86_64/build/venv/include -I/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c c-blosc/internal-complibs/zstd-1.5.5/compress/zstd_compress_sequences.c -o build/temp.macosx-10.9-x86_64-cpython-311/c-blosc/internal-complibs/zstd-1.5.5/compress/zstd_compress_sequences.o -g0 -Isrc -DH5_USE_18_API -DH5Acreate_vers=2 -DH5Aiterate_vers=2 -DH5Dcreate_vers=2 -DH5Dopen_vers=2 -DH5Eclear_vers=2 -DH5Eprint_vers=2 -DH5Epush_vers=2 -DH5Eset_auto_vers=2 -DH5Eget_auto_vers=2 -DH5Ewalk_vers=2 -DH5E_auto_t_vers=2 -DH5Gcreate_vers=2 -DH5Gopen_vers=2 -DH5Pget_filter_vers=2 -DH5Pget_filter_by_id_vers=2 -DH5Tarray_create_vers=2 -DH5Tget_array_dims_vers=2 -DH5Z_class_t_vers=2 -DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION -DSHUFFLE_SSE2_ENABLED -msse2
```

### #70

- true_cluster_id: 85
- predicted_cluster_id: 85
- confidence: 1.0
- true_template: `-- Looking for assert.h`
- matched_template: `-- Looking for assert.h`

**log**
```
-- Looking for strncasecmp
```

### #71

- true_cluster_id: 85
- predicted_cluster_id: 85
- confidence: 1.0
- true_template: `-- Looking for assert.h`
- matched_template: `-- Looking for assert.h`

**log**
```
-- Looking for ctime
```

### #72

- true_cluster_id: 85
- predicted_cluster_id: 85
- confidence: 1.0
- true_template: `-- Looking for assert.h`
- matched_template: `-- Looking for assert.h`

**log**
```
-- Looking for stdlib.h
```

### #73

- true_cluster_id: 5785
- predicted_cluster_id: 5785
- confidence: 1.0
- true_template: `[2Kreading sources... [ 1%] FAQ`
- matched_template: `[2Kreading sources... [ 1%] FAQ`

**log**
```
[2Kreading sources... [ 92%] usersguide/libref/structured_storage
```

### #74

- true_cluster_id: 5785
- predicted_cluster_id: 5785
- confidence: 1.0
- true_template: `[2Kreading sources... [ 1%] FAQ`
- matched_template: `[2Kreading sources... [ 1%] FAQ`

**log**
```
[2Kreading sources... [ 56%] release-notes/RELEASE_NOTES_v2.4.x
```

### #75

- true_cluster_id: 5785
- predicted_cluster_id: 5785
- confidence: 1.0
- true_template: `[2Kreading sources... [ 1%] FAQ`
- matched_template: `[2Kreading sources... [ 1%] FAQ`

**log**
```
[2Kreading sources... [ 91%] usersguide/libref/link_classes
```

### #76

- true_cluster_id: 5796
- predicted_cluster_id: 5796
- confidence: 1.0
- true_template: `[2Kwriting output... [ 1%] FAQ`
- matched_template: `[2Kwriting output... [ 1%] FAQ`

**log**
```
[2Kwriting output... [ 35%] release-notes/RELEASE_NOTES_v1.2
```

### #77

- true_cluster_id: 5796
- predicted_cluster_id: 5796
- confidence: 1.0
- true_template: `[2Kwriting output... [ 1%] FAQ`
- matched_template: `[2Kwriting output... [ 1%] FAQ`

**log**
```
[2Kwriting output... [ 92%] usersguide/libref/structured_storage
```

### #78

- true_cluster_id: 5796
- predicted_cluster_id: 5796
- confidence: 1.0
- true_template: `[2Kwriting output... [ 1%] FAQ`
- matched_template: `[2Kwriting output... [ 1%] FAQ`

**log**
```
[2Kwriting output... [ 99%] usersguide/usersguide
```

### #79

- true_cluster_id: 86
- predicted_cluster_id: 86
- confidence: 1.0
- true_template: `-- Looking for assert.h - found`
- matched_template: `-- Looking for assert.h - found`

**log**
```
-- Looking for fstat - found
```

### #80

- true_cluster_id: 86
- predicted_cluster_id: 86
- confidence: 1.0
- true_template: `-- Looking for assert.h - found`
- matched_template: `-- Looking for assert.h - found`

**log**
```
-- Looking for raise - found
```
