function curry(fn) {
  return function curried(...args) {
    if (fn.length > args.length) {
      return curried.bind(null, ...args);
    }
    return fn(...args)
  }
}

const join = (a, b, c) => {
  return `${a}_${b}_${c}`
}

const curriedJoin = curry(join)

console.log(curriedJoin(1, 2, 3), "test_1") // '1_2_3'

console.log(curriedJoin(1)(2, 3), "test_2") // '1_2_3'

console.log(curriedJoin(1, 2)(3), "test_2") // '1_2_3'