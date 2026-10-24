
document.addEventListener("DOMContentLoaded", () => {
    console.log("Cineon está listo.");

    const enlacesPeliculas = document.querySelectorAll(
        'a[href="#peliculas"]'
    );

    enlacesPeliculas.forEach((enlace) => {
        enlace.addEventListener("click", (evento) => {
            const catalogo = document.getElementById("peliculas");

            if (catalogo) {
                evento.preventDefault();

                catalogo.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

                history.replaceState(null, "", "#peliculas");
            }
        });
    });
});
