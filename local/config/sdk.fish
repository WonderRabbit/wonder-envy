# Keep the current session selection when sourcing SDKMAN's Bash functions.
function sdk --description 'Manage SDKMAN candidates through Bass'
    bass '__fish_sdk_path=$PATH; __fish_sdk_java=$JAVA_HOME; source "$SDKMAN_DIR/bin/sdkman-init.sh"; export PATH="$__fish_sdk_path" JAVA_HOME="$__fish_sdk_java"; unset __fish_sdk_path __fish_sdk_java; sdk' (string escape -- $argv)
end
