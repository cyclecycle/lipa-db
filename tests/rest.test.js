require('jest-extended')
const axios = require('axios')
const fs = require('fs')
const JSONStream = require('JSONStream')
const util = require('../util/util')


beforeAll(() => {
  const config = util.loadConfig()
  const url = config.db_rest_url
  console.log(url)
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
  expect.assertions(1)
  const url = global.url
  const queryUrl = `${url}/patterns`
  const payload = {
    'name': 'pattern 1',
    'role_pattern_instance': 'some_bytes',
  }
  return axios.post(queryUrl, payload)
    .then(response => {
      const item = response.data
      expect(item).toEqual(expect.toBeObject(item))
    })
})

test("Inserts a match", () => {
  expect.assertions(2)
  const url = global.url
  const matchesUrl = `${url}/matches`
  const payload = {
    sentence_id: 1,
    data: JSON.stringify({some: 'data'}),
  }
  return axios.post(matchesUrl, payload)
    .then(response => {
      const item = response.data
      expect(item).toEqual(expect.toBeObject(item))
      const matchId = item.id
      return matchId
    })
    .then(matchId => {
      const patternMatchesUrl = `${url}/pattern_matches`
      const payload = {
        'pattern_id': 2,  // Corresponds with pattern created above
        'match_id': matchId,
      }
      return axios.post(patternMatchesUrl, payload)
    })
    .then(response => {
      const item = response.data
      expect(item).toEqual(expect.toBeObject(item))
    })
})


// test("Deletes a pattern", () => {
//   expect.assertions(1)
//   const url = global.url
//   let queryUrl = `${url}/patterns`
//   return axios.get(queryUrl)
//     .then(response => {
//       return rowId = response.data[0].id
//     })
//     .then(rowId => {
//       queryUrl = `${url}/patterns?id=${rowId}`
//       return axios.delete(queryUrl)
//     })
//     .then(response => {
//       expect(response.status).toEqual(204)
//     })
// })


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


test("Fetches documents view", () => {
  expect.assertions(3)
  const url = global.url
  const queryUrl = `${url}/documents_view`
  return axios.get(queryUrl)
    .then(response => {
      const items = response.data  // Still returns Array
      const item = items[0]
      expect(items).toEqual(expect.toBeArray())
      expect(item.n_matches).toEqual(expect.toBeNumber())
      expect(item.n_sentences).toEqual(expect.toBeNumber())
    })
})

test("Fetches sentences view", () => {
  expect.assertions(2)
  const url = global.url
  const queryUrl = `${url}/sentences_view`
  return axios.get(queryUrl)
    .then(response => {
      const items = response.data  // Still returns Array
      const item = items[0]
      expect(items).toEqual(expect.toBeArray())
      expect(item.n_matches).toEqual(expect.toBeNumber())
    })
})

test("Fetches patterns view", () => {
  expect.assertions(2)
  const url = global.url
  const queryUrl = `${url}/patterns_view`
  return axios.get(queryUrl)
    .then(response => {
      const items = response.data  // Still returns Array
      const item = items[0]
      expect(items).toEqual(expect.toBeArray())
      expect(item.n_matches).toEqual(expect.toBeNumber())
    })
})

// test("Fetches pattern matches for a document", () => {
//   expect.assertions(2)
//   const url = global.url
//   const queryUrl = `${url}/pattern_matches_view/?document_id=1`
//   return axios.get(queryUrl)
//     .then(response => {
//       const items = response.data  // Still returns Array
//       // console.log(items.length)
//       // console.log(items)
//       const item = items[0]
//       expect(items).toEqual(expect.toBeArray())
//       // expect(item.sentence_data).toEqual(expect.toBeString())
//       expect(item.match_data).toEqual(expect.toBeString())
//     })
// })

// test("Fetches all matches", () => {
//   expect.assertions(1)
//   const url = global.url
//   const queryUrl = `${url}/matches`
//   return axios.get(queryUrl)
//     .then(response => {
//       const items = response.data
//       console.log(response.data)
//       const item = items[0]
//       expect(items).toEqual(expect.toBeArray())
//     })
// })

// test("Fetches all pattern matches", () => {
//   expect.assertions(1)
//   const url = global.url
//   const queryUrl = `${url}/pattern_matches_view`
//   return axios.get(queryUrl)
//     .then(response => {
//       const items = response.data
//       const item = items[0]
//       // console.log(items)
//       // console.log(items.length)
//       expect(items).toEqual(expect.toBeArray())
//     })
// })

test("Fetches pattern matches in chunks", () => {
  expect.assertions(2)
  const url = global.url
  const queryUrl = `${url}/pattern_matches_view`
  const nItems = 2
  const chunkSize = 2 // Minimum of 2
  const requests = []
  const rows = []
  for (i = 0; i < nItems; i = i + chunkSize) {
    const startRow = i
    const endRow = startRow + chunkSize - 1
    const params = {
      headers: {
        range: `rows=${startRow}-${endRow}`, // The range is inclusive
      },
    }
    const request = axios.get(queryUrl, params)
      .then(response => {
        const items = response.data
        items.forEach(item => {
          // console.log(item)
          rows.push(item)
        })
      })
      .catch((e) => {
        if (e.response.status == 416) {
          // Row range exceeded
        }
      })
    requests.push(request)
  }
  return axios.all(requests)
    .then(() => {
      expect(rows).toEqual(expect.toBeArray())
      expect(rows.length).toEqual(nItems)
    })
})


test("Fetches pattern matches in chunks until no more rows", () => {
  expect.assertions(2)
  const url = global.url
  const queryUrl = `${url}/pattern_matches_view`
  const chunkSize = 2 // Minimum of 2

  function buildRangeParamsObject (startRow, endRow) {
    const params = {
      headers: {
        range: `rows=${startRow}-${endRow}`, // The range is inclusive
      },
    }
    return params
  }

  function incrementChunkRange (startRow, endRow, chunkSize) {
    startRow = endRow + 1
    endRow = getEndRowValue(startRow, chunkSize)
    console.log({ startRow, endRow })
    return { startRow, endRow }
  }

  function incrementStartRowValue (startRow, endRow) {
    startRow = endRow + 1
    return startRow
  }

  function getEndRowValue (startRow, chunkSize) {
    const endRow = startRow + chunkSize - 1
    return endRow
  }

  function buildRecursiveRequest (queryUrl, startRow, chunkSize, resolve, reject, rows) {
    const endRow = getEndRowValue(startRow, chunkSize)
    const params = buildRangeParamsObject(startRow, endRow)
    const request = axios.get(queryUrl, params)
      .then(response => {
        const items = response.data
        items.forEach(item => {
          rows.push(items)
        })
        nextStartRow = incrementStartRowValue(startRow, endRow)
        const nextRequest = buildRecursiveRequest(queryUrl, nextStartRow, chunkSize, resolve, reject, rows)
        return nextRequest
      })
      .catch((e) => {
        if (e.response.status === 416) {
          resolve(rows)
        } else {
          throw e
        }
      })
    return request
  }

  function getRows (queryUrl, chunkSize) {
    if (chunkSize === undefined) {
      chunkSize = 2
    }
    const startRow = 0
    const rows = []
    const request = new Promise((resolve, reject) => {
      return buildRecursiveRequest(queryUrl, startRow, chunkSize, resolve, reject, rows)
    })
    return request
  }

  return getRows(queryUrl, chunkSize)
    .then((rows) => {
      expect(rows).toEqual(expect.toBeArray())
      expect(rows.length).toBeGreaterThanOrEqual(1)
    })
})


test("On delete pattern, corresponding matches are deleted", () => {
  expect.assertions(2)
  const url = global.url
  const queryUrl = `${url}/patterns/?id=2`
  return axios.delete(queryUrl)
    .then(response => {
      expect(response.status).toEqual(204)
    })
    .then(() => {
      const matchesQueryUrl = `${url}/pattern_matches/?pattern_id=2`
      return axios.get(matchesQueryUrl)
        .catch(e => {
          expect(e.response.status).toEqual(404)
        })
    })
})