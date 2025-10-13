class EmailSendException(Exception): pass # Erro durante o envio do e-mail.
class EmailTemplateInvalidException(Exception): pass # Erro ao preencher o template com as informações fornecidas.

class NotFoundError(Exception): pass # Informação não encontrado na base de dados, com base naquilo que o cliente envio para cá 
class EntityValidationError(Exception): pass # Houve erro no momento de validar e inserir as informações dos campos da Base de dados
class DuplicateReviewError(Exception): pass # Serve para informar de forma clara que a operação não é válida por duplicidade lógica, mesmo que a tabela não tenha nenhuma restrição UNIQUE.
class InvalidFields(Exception): pass # Está faltando campos obrigatórios para validar as informações
class UnknownError(Exception): pass # Erro que não pode identificado com base na programação provida por eu...
class ForeignKeyReferenceError(Exception): pass # Erro que lidar com erros de chave estrangeira inválida (ou qualquer referência inexistente)
class InvalidCredentialsException(Exception): pass # Erro que lidar com erros envolvendo login ou informações que não batem com que está cadastrado
class UnprocessableEntity(Exception): pass # é uma exceção que indica que o servidor entendeu a requisição (sintaxe ok), mas não 
                                            # conseguiu processá-la sem erro por causa de algum problema nos dados enviados.