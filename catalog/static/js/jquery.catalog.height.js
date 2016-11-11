/**
 * Created by Escsun on 11.11.2016.
 */
$(document).ready(function () {
    var heights = $(".parent").map(function () {
        return $(this).height();
    }).get(),
        maxHeight = Math.max.apply(null, heights);
    $(".child").height(maxHeight);
});
