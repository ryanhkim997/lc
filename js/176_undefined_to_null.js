// One of the differences between null and undefined is how they are treated differently in JSON.stringify().

// JSON.stringify({a: null})      // '{"a":null}'
// JSON.stringify({a: undefined}) // '{}'

// JSON.stringify([null])         // '[null]'
// JSON.stringify([undefined])    // '[null]'
// This difference might create troubles if there are missing alignments between client and server. It might be helpful to enforce using only one of them.

// You are asked to implement undefinedToNull() to return a copy that has all undefined replaced with null.

// undefinedToNull({a: undefined, b: 'BFE.dev'})
// // {a: null, b: 'BFE.dev'}

// undefinedToNull({a: ['BFE.dev', undefined, 'bigfrontend.dev']})
// // {a: ['BFE.dev', null, 'bigfrontend.dev']}

function undefinedToNull(arg) {
    if (arg === undefined) {
      return null;
    }
  
    if (Array.isArray(arg)) {
      return arg.map(undefinedToNull)
    } else if (typeof arg === "object") {
      for (let key in arg) {
        if (arg[key] === undefined) {
          arg[key] = null;
        } else if (typeof arg[key] === "object") {
          arg[key] = undefinedToNull(arg[key]);
        }
      }
    }
  
    return arg;
  }
  
  