require('jest-extended')
const axios = require('axios')


test("Fetches all documents", () => {
  expect.assertions(3)
  const url = 'http://localhost:8085/documents'
  return axios.get(url)
    .then(response => {
      const items = response.data
      const item = items[0]
      const itemId = item.id
      const itemData = JSON.parse(item.data)
      expect(items).toEqual(expect.toBeArray())
      expect(itemId).toEqual(expect.toBeNumber())
      expect(itemData).toEqual(expect.toBeObject())
    })
})


test("Fetches one document", () => {
  expect.assertions(3)
  const url = 'http://localhost:8085/documents/?id=1'
  return axios.get(url)
    .then(response => {
      const items = response.data  // Still returns Array
      const item = items[0]
      const itemId = item.id
      const itemData = JSON.parse(item.data)
      expect(items).toEqual(expect.toBeArray())
      expect(itemId).toEqual(expect.toBeNumber())
      expect(itemData).toEqual(expect.toBeObject())
    })
})


test("Inserts a pattern", () => {
  expect.assertions(2)
  const url = 'http://localhost:8085/patterns/'
  const patternData = {'some': 'pattern data'}
  const payload = {'data': JSON.stringify(patternData)}
  return axios.post(url, payload)
    .then(response => {
      const item = response.data
      const itemData = JSON.parse(item.data)
      expect(item).toEqual(expect.toBeObject(item))
      expect(itemData).toEqual(expect.toBeObject())
    })
})


test("Deletes a pattern", async () => {
  expect.assertions(1)
  let url = 'http://localhost:8085/patterns'
  return axios.get(url)
    .then(response => {
      return rowId = response.data[0].id
    })
    .then(rowId => {
      url = `http://localhost:8085/patterns?id=${rowId}`
      return axios.delete(url)
    })
    .then(response => {
      expect(response.status).toEqual(204)
    })
})
