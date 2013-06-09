(function () {
    if (document.querySelector) {
        var $ = document.querySelector.bind(document),
            $$ = document.querySelectorAll.bind(document),
            body = $('body'),
            header = $('header'),
            headerHeight = header.clientHeight,
            headerBackgroundTop = 25,
            headerBackgroundBottom = 75,
            headerBackgroundRange = 100 / (headerBackgroundBottom - headerBackgroundTop);

        document.addEventListener('scroll', function (evt) {
            var yMovement;

            if (body.scrollTop <= headerHeight) {
                yMovement = (body.scrollTop / headerHeight) * 100;
                yMovement = yMovement / headerBackgroundRange;
                yMovement = yMovement + headerBackgroundTop;
                header.style.backgroundPositionY = yMovement + '%';
            }
        });
    }
}());