# Existing nvm-sh installation, bridged into the current Fish environment.
function nvm --description 'Manage Node with nvm-sh through Bass'
    bass 'source "$NVM_DIR/nvm.sh" --no-use; nvm' (string escape -- $argv)
end
