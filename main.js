getInput = setInterval(() => {


    let $btnStgo = d.querySelector("#shipping_method_0_flat_rate3")
    

    if ($btnStgo) {
        clearInterval(getInput)
        console.log("Hola , el intervalo ha terminado")
        let d = document;
        d.addEventListener("click", e => {
        console.log(e.target.value)
            if (e.target.value == "flat_rate:3"){
                console.log("clickComunasCercanas")
            } 
            else if (e.target.value== "flat_rate:5") {
                    console.log("clickComunasLejanas")

            }
            

        })
    }
    
}, 1000)