require('jest-extended')
const axios = require('axios')
const fs = require('fs')


beforeAll(() => {
  const url = 'http://localhost:8086'  // TODO import from config
  global.url = url
})


test("Fetches all documents", () => {
  expect.assertions(3)
  const url = global.url
  const queryUrl = `${url}/documents`
  return axios.get(queryUrl)
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
  const url = global.url
  const queryUrl = `${url}/documents/?id=1`
  return axios.get(queryUrl)
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
  const url = global.url
  const queryUrl = `${url}/patterns/`
  const patternData = {'some': 'pattern data'}
  const payload = {
    'name': 'pattern 1',
    'pattern_data': JSON.stringify(patternData),
  }
  return axios.post(queryUrl, payload)
    .then(response => {
      const item = response.data
      const itemData = JSON.parse(item.pattern_data)
      expect(item).toEqual(expect.toBeObject(item))
      expect(itemData).toEqual(expect.toBeObject())
    })
})


test("Deletes a pattern", () => {
  expect.assertions(1)
  const url = global.url
  let queryUrl = `${url}/patterns`
  return axios.get(queryUrl)
    .then(response => {
      return rowId = response.data[0].id
    })
    .then(rowId => {
      queryUrl = `${url}/patterns?id=${rowId}`
      return axios.delete(queryUrl)
    })
    .then(response => {
      expect(response.status).toEqual(204)
    })
})


test("Fetches sentences associated with document", () => {
  expect.assertions(4)
  const documentId = 1
  const url = global.url
  let queryUrl = `${url}/sentences/?document_id=${documentId}`
  return axios.get(queryUrl)
    .then(response => {
      const items = response.data
      const item = items[0]
      const itemId = item.id
      const itemData = JSON.parse(item.data)
      expect(items).toEqual(expect.toBeArray())
      expect(item).toEqual(expect.toBeObject())
      expect(itemId).toEqual(expect.toBeNumber())
      expect(itemData).toEqual(expect.toBeObject())
    })
})

test("Fetches tokens associated with sentence", () => {
  expect.assertions(4)
  const sentenceId = 1
  const url = global.url
  let queryUrl = `${url}/tokens/?sentence_id=${sentenceId}`
  return axios.get(queryUrl)
    .then(response => {
      const items = response.data
      const item = items[0]
      const itemId = item.id
      const itemData = JSON.parse(item.data)
      expect(items).toEqual(expect.toBeArray())
      expect(item).toEqual(expect.toBeObject())
      expect(itemId).toEqual(expect.toBeNumber())
      expect(itemData).toEqual(expect.toBeObject())
    })
})

