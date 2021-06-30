

<script>
    

let checkoutWindow = window.location.href
if (checkoutWindow == "https://moyidesigns.cl/checkout/") {

    getMercado = setTimeout(()=> {
        let $listaMercado = document.getElementsByClassName("woocommerce-checkout-payment")
        if ($listaMercado) {
            let btnMercado = document.getElementById("payment_method_woo-mercado-pago-basic")
            btnMercado.addEventListener("click", e => {
                alert("Hola")
            })

        }
    }, 100)

    } else {
    console.log("No estamos en checkout window")
    }
        
</script>
     


     getMercado = setTimeout(()=> {
        let $listaMercado = document.getElementsByClassName("woocommerce-checkout-payment")
        if ($listaMercado) {
            console.log("hay listaMercado")
            console.log($listaMercado)
            clearInterval(getMercado)
            let btnMercado = document.getElementById("payment_method_woo-mercado-pago-basic")
            document.addEventListener("click", e => {
               alert(e.target.value)
               if(e.target == btnMercado) {
                 alert("click")
               }
             })

        }
    }, 100)
    getMercado = setTimeout(()=> {
        let $listaMercado = document.getElementsByClassName("woocommerce-checkout-payment")
        if ($listaMercado) {
            console.log("hay listaMercado")
            console.log($listaMercado)
            clearInterval(getMercado)
            let btnMercado = document.getElementById("payment_method_woo-mercado-pago-basic")
            document.addEventListener("click", e => {
               alert(e.target.value)
               if(e.target == btnMercado) {
                 alert("click")
               }
             })

        }
    }, 100)
    getMercado = setTimeout(()=> {
        let $listaMercado = document.getElementsByClassName("woocommerce-checkout-payment")
        if ($listaMercado) {
            console.log("hay listaMercado")
            console.log($listaMercado)
            clearInterval(getMercado)
            let btnMercado = document.getElementById("payment_method_woo-mercado-pago-basic")
            document.addEventListener("click", e => {
               alert(e.target.value)
               if(e.target == btnMercado) {
                 alert("click")
               }
             })

        }
    }, 100)
    


