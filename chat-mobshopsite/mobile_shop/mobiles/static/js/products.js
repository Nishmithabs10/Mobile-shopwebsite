
fetch("/static/data/products.json").then(function(response) {
    return response.json();
}).then(function(response) {
    const products = response.products;
    let placeholder = document.querySelector("#products");
    placeholder.classList.add("row");

    for(let i = 0; i < products.length; i++) {

        let product = products[i];

        const divCol = document.createElement("div");
        divCol.classList.add("col"); // Div column

        const divCard = document.createElement("div"); // Div Card
        divCard.classList.add("card");
        divCard.style.width = "18rem";

        const imageElement = document.createElement("img");
        imageElement.classList.add("card-img-top");
        imageElement.src = product.image;
        imageElement.alt = product.title;

        const divCardBody = document.createElement("div");
        divCardBody.classList.add("card-body");

        const titleElement = document.createElement("h5");
        titleElement.classList.add("card-title");
        titleElement.innerText = product.title;

        const descriptionElement = document.createElement("p");
        descriptionElement.classList.add("card-text");
        descriptionElement.innerText = product.description;

        const buttonElement = document.createElement("a");
        buttonElement.classList.add("btn", "btn-primary");
        buttonElement.innerText = "Buy for $" + product.price;
        buttonElement.href = "#";


        // Card body elements
        divCardBody.appendChild(titleElement);
        divCardBody.appendChild(descriptionElement);
        divCardBody.appendChild(buttonElement);

        divCard.appendChild(imageElement);
        divCard.appendChild(divCardBody);

        divCol.appendChild(divCard);

        placeholder.appendChild(divCol);
    }
});