file(REMOVE_RECURSE
  "cartographer_rviz_automoc.cpp"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/actionlib_generate_messages_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
