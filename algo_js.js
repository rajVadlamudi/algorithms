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