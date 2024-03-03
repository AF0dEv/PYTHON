$(document).ready(function() {
    $('.edit-button').on('click', function() {
        var id = $(this).data('id');
        var descricao = $(this).data('descricao');
        var userId = $(this).data('user-id');
        // Update the form action URL based on the userId
        $('#ModalEditTarefaAdmin form').attr('action', 'userAdminUpdateDescAdmin/' + userId);
        // Update the form fields based on the data attributes
        $('#ModalEditTarefaAdmin form input[name="id_tarefa"]').val(id);
        $('#ModalEditTarefaAdmin form input[name="descricao"]').val(descricao);
        $('#ModalEditTarefaAdmin form input[name="user_id"]').val(userId);
    });
});