const food = document.getElementById("food")
const obstacle = document.getElementById("obstacle")
const path = document.getElementById("path")
const hill = document.getElementById("hill")
const btn = [food, obstacle, path, hill]


const xInput = document.getElementById("x")
const yInput = document.getElementById("y")
const createMapHtml = document.getElementById("createMap")
const map = document.getElementById('map')
const save = document.getElementById("save")
const nameMap = document.getElementById("name")

save.addEventListener("click", () => {
    saveMap()
})

let activeMode = "path"

food.addEventListener("click", () => {
    btn.forEach(el => {
        if (el === food){
            el.classList = "on"
        }else{
            el.classList = ""
        }
    })
    activeMode = "food"
})  

obstacle.addEventListener("click", () => {
        btn.forEach(el => {
        if (el === obstacle){
            el.classList = "on"
        }else{
            el.classList = ""
        }
    })
    activeMode = "obstacle"
})

path.addEventListener("click", () => {
        btn.forEach(el => {
        if (el === path){
            el.classList = "on"
        }else{
            el.classList = ""
        }
    })
    activeMode = "path"
})

hill.addEventListener("click", () => {
    
        btn.forEach(el => {
        if (el === hill){
            el.classList = "on"
        }else{
            el.classList = ""
        }
    })
    activeMode = "hill"
})


function changeCellule(cel, activeMode){
    console.log(cel, "touché")
    if (activeMode === "obstacle"){
        console.log(cel.className)
        if (cel.className == 'cellule obstacle'){
            cel.className = 'cellule path' // inverse case
        }else {
            cel.className = 'cellule obstacle' // met case a obstacle
        }
        
    }if (activeMode === "path"){
        if (cel.className == 'cellule path'){
            cel.className = 'cellule obstacle' // inverse case
        }else {
            cel.className = 'cellule path' // met case a obstacle
        }
    }if (activeMode === "food"){
        if (cel.className == 'cellule food'){
            cel.className = 'cellule path'
        }else {
            cel.className = 'cellule food'
        }
    }if (activeMode === "hill"){
        cel.className = 'cellule hill' 
    }
}


function createMap(y, x){
    map.innerHTML = ""
    if (y == 0 && x == 0 || typeof Number(y) === NaN  || typeof Number(x) === NaN || x === "de"){ 
        x = 3;
        y = 3;
    }
    for (let i=0;i < y; i++){
        row = document.createElement("div")
        row.id = "row" + i
        row.className = "row"
        for (let j = 0; j < x; j++){
            let cellule = document.createElement("div")
            cellule.className = "cellule"
            cellule.classList.add("path") // faire des cellules type chemin a l'init
            row.appendChild(cellule)
        }
        map.appendChild(row)
    }
}


createMapHtml.addEventListener("click", () => {
    createMap(xInput.value, yInput.value)

    let cellule = document.querySelectorAll(".cellule")
    cellule.forEach(el => {
        el.addEventListener("click", () => {
            console.log(el)
            changeCellule(el, activeMode);
        })
    })

})


function saveMap(){
    let MAP = {
    "map" : [],
    "width":"",
    "height":"",
    "hill":"",
    "name":""
}
    console.log(map)
    let rows =  map.querySelectorAll(".row")
    console.log(rows.length)
    for (let i = 0; i < rows.length; i ++){
        console.log(rows[i]);
        console.log(rows.length)
        rowsJson = []
        //for (let j = 0; j < rows.length; j++){
        allCelluleOfRow = rows[i].querySelectorAll(".cellule")
        let j = 0
        allCelluleOfRow.forEach(cel => {
            console.log(cel);
            let value // valeur a ajouté
            console.log(cel.classList.value);
                if (cel.classList.value === "cellule path"){
                    value = 1
                }if (cel.classList.value === "cellule obstacle"){
                    value = "X"
                }if (cel.classList.value === "cellule food"){
                    value = "f"
                }if (cel.classList.value === "cellule hill"){
                    value = "h"; // h pour home
                    MAP["hill"] = [i, j]; // y,x
                }
                rowsJson.push(value);
                j += 1;
        })
        MAP["map"].push(rowsJson); // "map" change jamais
        MAP["width"] = allCelluleOfRow.length;
        MAP["height"] = rows.length;
        MAP["name"] = nameMap.value // si vide alors custom=custom_map

        }
        console.log(MAP);
        let dl = document.createElement('a')
        dl.download = nameMap.value+'.json' // target filename
        dl.href = `data:application/json;charset=utf-8,${JSON.stringify(MAP)}`
        dl.click()
}

