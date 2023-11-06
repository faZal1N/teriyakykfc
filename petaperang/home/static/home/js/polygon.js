ymaps.ready(init);
massiv_a=[
                // Координаты вершин внешнего контура.
                [
                    [55.75, 37.80],
                    [55.80, 37.90],
                    [55.75, 38.00],
                    [55.70, 38.00],
                    [55.70, 37.80]
                ],
                // Координаты вершин внутреннего контура.
                [
                    [55.75, 37.82],
                    [55.75, 37.98],
                    [55.65, 37.90]
                ]
            ];
Massiv_b=[
                // Координаты вершин внешнего контура.
                [
                    [55.75, 37.80],
                    [55.80, 37.90],
                    [55.75, 38.00],
                    [55.70, 38.00],
                    [55.70, 37.80]
                ],
                // Координаты вершин внутреннего контура.
                [
                    [55.75, 37.82],
                    [55.75, 37.98],
                    [55.65, 37.90]
                ]
            ];



function init() {

    var myMap = new ymaps.Map("map", {
            center: [55.73, 37.75],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        });

    // Создаем многоугольник, используя класс GeoObject.
    var myGeoObject = new ymaps.GeoObject({
        // Описываем геометрию геообъекта.
        geometry: {
            // Тип геометрии - "Многоугольник".
            type: "Polygon",
            // Указываем координаты вершин многоугольника.
            coordinates: massiv_a,
            // Задаем правило заливки внутренних контуров по алгоритму "nonZero".
            fillRule: "nonZero"
        },
        // Описываем свойства геообъекта.
        properties:{
            // Содержимое балуна.
            balloonContent: "Многоугольник"
        }
    }, {
        // Описываем опции геообъекта.
        // Цвет заливки.
        fillColor: '#00FF00',
        // Цвет обводки.
        strokeColor: '#0000FF',
        // Общая прозрачность (как для заливки, так и для обводки).
        opacity: 0.5,
        // Ширина обводки.
        strokeWidth: 5,
        // Стиль обводки.
        strokeStyle: 'shortdash'
    });

    // Добавляем многоугольник на карту.
    myMap.geoObjects.add(myGeoObject);

    // Создаем многоугольник, используя вспомогательный класс Polygon.
    var myPolygon = new ymaps.Polygon([
        // Указываем координаты вершин многоугольника.
        // Координаты вершин внешнего контура.
        [
            [55.75, 37.50],
            [55.80, 37.60],
            [55.75, 37.70],
            [55.70, 37.70],
            [55.70, 37.50]
        ],
        // Координаты вершин внутреннего контура.
        [
            [55.75, 37.52],
            [55.75, 37.68],
            [55.65, 37.60]
        ]
    ], {
        // Описываем свойства геообъекта.
        // Содержимое балуна.
        hintContent: "Многоугольник"
    }, {
        // Задаем опции геообъекта.
        // Цвет заливки.
        fillColor: '#00FF0088',
        // Ширина обводки.
        strokeWidth: 5
    });

    // Добавляем многоугольник на карту.
    myMap.geoObjects.add(myPolygon);




    let i = 37.820
        setInterval(function () {
                    myGeoObject.geometry.setCoordinates ([
                    // Координаты вершин внешнего контура.
                    [
                        [55.75, 37.80],
                        [55.80, 37.90],
                        [55.75, 38.00],
                        [55.70, 38.00],
                        [55.70, 37.80]
                    ],
                    // Координаты вершин внутреннего контура.
                    [
                        [55.75, i],
                        [55.75, 37.98],
                        [55.65, 37.90]
                    ]
                ]
             );
             i+=0.001
        //console.log (myGeoObject.geometry);
        //console.log (i);
        }, 1);
}
