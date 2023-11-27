// dataFetcher.js
let places;

function fetchData(jsonUrl) {
    return fetch(jsonUrl)
        .then((res) => res.json())
        .then((jsonData) => {
            places = jsonData;
        })
        .catch((error) => console.error("Error fetching JSON:", error));
}