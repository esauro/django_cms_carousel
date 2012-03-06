jQuery(function($) {
    $('#carouseltab_set-group').sortable({
        /*containment: 'parent',
        zindex: 10, */
        items: 'div.inline-related',
        handle: 'h3:first',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('input[id$=title]').val()) {
                    $(this).find('input[id$=order]').val(i+1);
                }
            });
        }
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('fieldset').hide();
    
    $('div.inline-related h3').prepend('<span style="color:#AAA;">Glisser pour trier </span>');
    
    $('div.inline-related h3').append('<span name="edit" style="color:#AAA;">Cliquez pour éditer </span>');
    
    $('div.inline-related').find('input[id$=order]').parent('div').hide();
    $('div.inline-related h3 ').find('span[name$=edit]').click(
        function(){
            $(this).parent().parent().find('fieldset').toggle("slow");
        });
});