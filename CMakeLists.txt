# Iliad Project Build File

cmake_minimum_required (VERSION 2.6)

project(iliad)

set (ILIAD_VERSION_MAJOR 1)
set (ILIAD_VERSION_MINOR 0)

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG -Wall -Werror")

configure_file (
  "${PROJECT_SOURCE_DIR}/include/iliad.hpp.in"
  "${PROJECT_BINARY_DIR}/include/iliad.hpp"
  )

include_directories("include" "${PROJECT_BINARY_DIR}/include")

set(CGI_HEADER_FILES
  include/cgi/log.hpp
  include/cgi/request.hpp
  include/cgi/response.hpp
  include/cgi/server.hpp
)

set(HEADER_FILES
  include/exception.hpp
  include/log.hpp
  include/request.hpp
  include/response.hpp
  include/server.hpp
  include/loader.hpp
  include/package.hpp
  include/core/loader.hpp
  include/core/config/package.hpp
  include/core/storage/package.hpp
)

set(CGI_SOURCE_FILES
  src/cgi/main.cpp
  src/cgi/log.cpp
  src/cgi/request.cpp
)

set(SOURCE_FILES
  src/server.cpp
  src/log.cpp
  src/request.cpp
  src/response.cpp
  src/loader.cpp
  src/package.cpp
  src/core/loader.cpp
  src/core/config/package.cpp
  src/core/storage/package.cpp
)

add_executable(iliad-cgi ${HEADER_FILES} ${SOURCE_FILES} ${CGI_HEADER_FILES} ${CGI_SOURCE_FILES})

INSTALL(TARGETS iliad-cgi DESTINATION /usr/lib/cgi-bin)
