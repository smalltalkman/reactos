include_directories(${REACTOS_SOURCE_DIR}/include/reactos/drivers
                    inc)

list(APPEND SOURCE
    src/block.c
    src/cleanup.c
    src/close.c
    src/cmcb.c
    src/create.c
    src/debug.c
    src/devctl.c
    src/dirctl.c
    src/dispatch.c
    src/except.c
    src/fastio.c
    src/ffs.c
    src/fileinfo.c
    src/flush.c
    src/fsctl.c
    src/init.c
    src/lock.c
    src/memory.c
    src/misc.c
    src/pnp.c
    src/read.c
    src/shutdown.c
    src/volinfo.c
    src/write.c
    inc/ffsdrv.h)

add_library(ffs MODULE ${SOURCE} src/ffsdrv.rc)

if(USE_CLANG_CL OR (NOT MSVC))
    target_compile_options(ffs PRIVATE -Wno-pointer-sign -Wno-unused-function)
    target_compile_options(ffs PRIVATE -Wno-unused-variable -Wno-missing-braces)
    if(USE_CLANG_CL)
        target_compile_options(ffs PRIVATE -Wno-empty-body)
    endif()
endif()

if(CMAKE_C_COMPILER_ID STREQUAL "GNU")
    target_compile_options(ffs PRIVATE -Wno-unused-but-set-variable)
endif()

add_definitions(-D__KERNEL__)
set_module_type(ffs kernelmodedriver)
target_link_libraries(ffs memcmp ${PSEH_LIB})
add_importlibs(ffs ntoskrnl hal)
add_pch(ffs inc/ffsdrv.h SOURCE)
add_cd_file(TARGET ffs DESTINATION reactos/system32/drivers FOR all)

