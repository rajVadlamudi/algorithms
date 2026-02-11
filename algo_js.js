//command: node algo_js.js

const factorial = (n)=>{
    let result = 1
    for(i=1; i<=n; i++) result *=i
    return result
}
let test = 3
console.log(`factorial(${test}):${factorial(test)}`)

const sort = (arr)=>{
    let result = []
    let min = 0
    let index = 0
    while(arr.length>0){
        index = 0
        min = arr[index]
        for(i=1; i<arr.length; i++){
            if(arr[i]<min){
                min = arr[i]
                index = i
            }
        }
        result.push(min)
        arr.splice(index,1)
    }   
    return result
}
test = [5,3,2,4,1]
console.log(`sort(${test}):${sort(test)}`)

const sum = (arr)=>{
    let result = []
    arr.flat()
    for(let i=0; i<arr.length-1; i++) result.push(Number(arr[i])+Number(arr[i+1]))
    return result
}

const pascal = (n)=>{
    let result = []
    let temp = []
    for(let i=0; i<=Number(n); i++){
        console.log('i:'+i);
        i===0 ? result.push(1) : i===1 ? result.push([1,1]) : result.push([1,...sum(result[i-1]),1]); 
    }
    return result
}
test = 5
// console.log(`sum(${test}):${sum(test)}`)
console.log(`pascal(${test}):${pascal(test)}`)