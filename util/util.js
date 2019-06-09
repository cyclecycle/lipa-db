const fs = require('fs')

const CONFIG_PATH = 'config.json'

function loadConfig() {
  const content = fs.readFileSync(CONFIG_PATH)
  const config = JSON.parse(content)
  return config
}

module.exports = {
  loadConfig: loadConfig,
}