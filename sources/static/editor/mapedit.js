const food = document.getElementById("food");
const obstacle = document.getElementById("obstacle");
const path = document.getElementById("path");
const hill = document.getElementById("hill");
const btn = [food, obstacle, path, hill];

const xInput = document.getElementById("x");
const yInput = document.getElementById("y");
const createMapHtml = document.getElementById("createMap");
const map = document.getElementById("map");
const save = document.getElementById("save");
const nameMap = document.getElementById("name");
const sizeInput = document.getElementById("size");
const elem = document.getElementById("inputFile");
const killBtn = document.getElementById("killMi");
const minimizeBtn = document.getElementById("minimizeBtn");


let sizeCellule = Number(sizeInput.value);
let activeMode = "obstacle";

let leftDown = false;
let rightDown = false;
let centerDown = false;
let cellule 

btn.forEach(el => { //pour tout les btn s'occupe de listener et de l'affichage
    el.addEventListener("click", () => {
        btn.forEach(style => {
            if (style == el){
                el.classList.add("on");
                activeMode = el.id; 
            }else {
                style.classList.remove("on");
            }
        });
    })
});



sizeInput.addEventListener("input", () => {
    console.log(`size : ${sizeInput.value}`);
    sizeCellule = Number(sizeInput.value);
    console.log(sizeCellule);
    updateSizeCellule(sizeCellule);
})

document.addEventListener("wheel", (event) => {
    const up = 5;
    const down = -5;
    const value = (event.deltaY < 0) ? up : down;
    sizeCellule +=value
    sizeCellule = Math.max(Math.min(sizeCellule,100 ), 1 );
    updateSizeCellule(sizeCellule);
    sizeInput.value = sizeCellule
    console.log(sizeCellule);
});



function updateSizeCellule(size) {
    document.querySelectorAll(".cellule").forEach(el => {
        el.style.width = `${size}px`;
        el.style.height = `${size}px`;
    })
}



function importMap(mapJson) {
    map.innerHTML = ""; // reset map
    
    for (let i=0;i < mapJson.height; i++){
        row = document.createElement("div");
        row.id = `row${i}`;
        row.className = "row";
        for (let j = 0; j < mapJson.width; j++){
            let cellule = document.createElement("div");
            cellule.className = "cellule";
            cellule.style.width = `${sizeCellule}px`;
            cellule.style.height = `${sizeCellule}px`;
            cellule.classList.add(jsonCelluleToClass(mapJson.map[i][j])); // cellules de type chemin a l'init
            row.appendChild(cellule);
        }
        map.appendChild(row);
    }
    cellule = document.querySelectorAll(".cellule");
};



function jsonCelluleToClass(el) {
    if (typeof el  === "number"){return "path"};
    if (el === "X"){return "obstacle"};
    if (el === "h"){return "hill"};
    if (el === "f"){return "food"};
}




function createMap(y, x){
    map.innerHTML = ""; // reset map
    if (y == 0 && x == 0 || typeof Number(y) === NaN  || typeof Number(x) === NaN || x === "" || y === ""){ 
        x = 10;
        y = 10;
    }
    for (let i=0;i < y; i++){
        row = document.createElement("div");
        row.id = `row${i}`;
        row.className = "row";
        for (let j = 0; j < x; j++){
            let cellule = document.createElement("div");
            cellule.className = "cellule";
            cellule.style.width = `${sizeCellule}px`;
            cellule.style.height = `${sizeCellule}px`;
            cellule.classList.add("path"); // cellules de type chemin a l'init
            row.appendChild(cellule);
        }
        map.appendChild(row);
    }
}


function changeCellule(cel, activeMode){
    console.log(cel, "touché");
    if (activeMode === "obstacle"){
        cel.className = 'cellule obstacle'; // met case à "obstacle"
    }
    if (activeMode === "path"){
        cel.className = 'cellule path'; // met case à "path"
    }
    if (activeMode === "food"){
        cel.className = 'cellule food'; // met case à "food"
    }
    if (activeMode === "hill"){
        cel.className = 'cellule hill'; // met case à "hill"
    }
}



function saveMap(){
    
    let have_hill = false;
    let MAP = {
    "map" : [],
    "width":"",
    "height":"",
    "hill":"",
    "name":""
    };
    
    let rows =  map.querySelectorAll(".row");
    for (let i = 0; i < rows.length; i ++){
        //console.log(rows[i]);
        //console.log(rows.length)
        rowsJson = [];
        //for (let j = 0; j < rows.length; j++){
        let allCelluleOfRow = rows[i].querySelectorAll(".cellule");
        let j = 0;
        allCelluleOfRow.forEach(cel => {
            console.log(cel);
            let value; // valeur a ajouté
            //console.log(cel.classList.value);
                if (cel.classList.value === "cellule path"){
                    value = 1;
                }if (cel.classList.value === "cellule obstacle"){
                    value = "X";
                }if (cel.classList.value === "cellule food"){
                    value = "f";
                }if (cel.classList.value === "cellule hill" && have_hill === true){
                    value = 1;
                }
                if (cel.classList.value === "cellule hill" && have_hill === false){
                    value = "h"; // h pour home
                    MAP["hill"] = [i, j]; // y,x
                    have_hill = true;
                }
                rowsJson.push(value);
                j += 1;
        })
        MAP["map"].push(rowsJson); // "map" change jamais
    }
    MAP["width"] = rows[0].querySelectorAll(".cellule").length;
    MAP["height"] = rows.length;
    let name = prompt("Nom de la map ?", "custom_map") || "custom_map";
    // let name = input()
    MAP["name"] = name;

    console.log(MAP);
    alert("Pour evitez les erreurs assurez vous d'avoir mis une cellule nourriture et maison");
    return MAP;
}


// recup tout les el html .cellule
function resetCellListeners() {
    cellule = document.querySelectorAll(".cellule");

    cellule.forEach(el => {
        el.addEventListener("click", () => {
            changeCellule(el, activeMode);
        });

        el.addEventListener("mouseover", () => {
            if (leftDown) {
                changeCellule(el, activeMode);
            }
            if (rightDown) {
                changeCellule(el,"path" ) // met case neutre
            }
        });

    });
}
// boucle principale
createMapHtml.addEventListener("click", () => {
    createMap(xInput.value, yInput.value);
    resetCellListeners()
})
//en dehors de boucle main car peut etre activé avant/sans créer une map
elem.type = "file";
let jsonData = null;
elem.addEventListener("change", async () => {
    console.log("jdpezh");
if (elem.files.length === 1) {
    const file = elem.files[0];
    const text = await file.text();   // lire le fichier
    jsonData = JSON.parse(text);      // convertir en objet JS
    console.log(`Map ${jsonData.name} importé`);

    importMap(jsonData)
    resetCellListeners()
    }
});


windowsFull = true
const windowEl = document.getElementById("window");
console.log(windowEl);
minimizeBtn.addEventListener("click", () => {
    let action = windowsFull ?  "translateX(-14em)" : "translateX(1px)"; //condition ? exprSiVrai : exprSiFaux;
    let ch = windowsFull ? "❯" : "❮" ;
    console.log(action);
    windowEl.style.transform = action;
    minimizeBtn.textContent = ch
    windowsFull = !windowsFull
    })





let mouve = null

let mapX = 0
let mapY = 0

let originX = 0
let originY = 0

let lastX = 0
let lastY = 0



function getdegreeFromRad(rad) {
  return rad  * (180/Math.PI)
}

//bloquer clic droit qui affiche menu u navigateur
document.addEventListener("contextmenu", (event) => {
    event.preventDefault()
})


let antX = 500;
let antY = 500;
const bubule = document.getElementById("bubbleDeMi");
bubule.style.display = "none"; //init
//33 et 67 sont juste des constantes pour bien cadré la bubule de XXX
bubule.style.left = antX - 33 + "px";
bubule.style.top = antY - 67 + "px";
const antDiv = document.getElementById("ant");
antDiv.style.left = antX+"px"
antDiv.style.top = antY+"px"
let intervalId = null;
antDiv.style.transform = "rotate(90deg)"
function moveAnt(x, y) {
  if (intervalId) clearInterval(intervalId);
  intervalId = setInterval(() => {
    let dx = x - antX;
    let dy = y - antY;
    let distance = Math.sqrt(dx * dx + dy * dy);

    if (distance < 2) {
      clearInterval(intervalId);
      return;
    }

    let speed = 3;
    antX += (dx / distance) * speed;
    antY += (dy / distance) * speed;

    antDiv.style.left = antX + "px";
    antDiv.style.top = antY + "px";
    bubule.style.left = antX - 33 + "px";
    bubule.style.top = antY - 67 +  "px";
    let rad = Math.atan2(dy, dx);
    let deg = rad * (180 / Math.PI);
    deg += 90
    antDiv.style.transform = "rotate(" + deg + "deg)";
  }, 16); 
}


antDiv.addEventListener("mouseover", () => {
    bubule.style.display = "block";
});
antDiv.addEventListener("mouseout", () => {
    bubule.style.display = "none";
});

killBtn.addEventListener("click" ,() => {
    antDiv.style.display = "none";
    killBtn.remove()
    console.log("Mi est triste :(");
});

document.addEventListener("mousedown", (event) => {
    if (event.button === 0) {
        leftDown = true
        console.log("clic gauche enfoncé")
        moveAnt(event.clientX, event.clientY)
    }
    if (event.button === 1) {
        centerDown = true;
        document.body.style.cursor = "grabbing"
        map.style.cursor = "grabbing"
        console.log("clic droit enfoncé")
        // position curseur quand clic enfoncé
        originX = event.clientX
        originY = event.clientY

        mouve = function (event) {
            lastX = event.clientX
            lastY = event.clientY
            let difX = originX - lastX
            let difY = originY - lastY
            map.style.transform = `translate(${-difX - mapX}px, ${-difY - mapY}px)` }
            //bouge map de différence entre position de départ et position actuelle
            // mapX / mapY 
        document.addEventListener("mousemove", mouve) 
    }if (event.button === 2) {
        rightDown = true
    }
})

document.addEventListener("mouseup", (event) => {
    if (event.button === 0) {
        leftDown = false
        console.log("clic gauche relâché")
    }if (event.button === 1) {
        centerDown = false
        console.log("clic droit relâché")
        map.style.cursor = "cell"
        document.body.style.cursor = "auto"
        document.removeEventListener("mousemove", mouve)
        let difX = originX - lastX
        let difY = originY - lastY
        mapX += difX
        mapY += difY
    }if (event.button === 2) {
        rightDown = false
        console.log("clic droit relâché")
    }
})



const form = document.querySelector("form");

form.addEventListener("submit", function (e) {
    e.preventDefault(); // ⛔ bloque l'envoi immédiat

    // 👉 calcul de ta map (si lourd)
    const mapData = saveMap(); // exemple

    document.getElementById("mapData").value = JSON.stringify(mapData);

    // ✅ maintenant on envoie pour de vrai
    form.submit();
});