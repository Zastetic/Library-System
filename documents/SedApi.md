# Como usar a API da SED

As APIs da SED serão usadas para termos informações de alunos de forma dinâmica e prática.

Para isso, é necessario realizar o login, e após ultilizar uma API que retorna informações do aluno.

## Realizando login
Body necessário para requisição
```bash
{
        "usuario": user,
        "senha": passw,
        "tipo": 'A',
        "__RequestVerificationToken": "1dKtpA4KwupanBFmiP7qJw6"
    }
```
API de login. Retorna cookies de sessão.
```http
POST https://sed.educacao.sp.gov.br/Logon/Logon/
```

## Informações do aluno:
Com os cookies da API de login na sessão, essa API retorna diversas informações relacionadas ao Estudante como nome, RA, cpf, idade.
```http
POST https://sed.educacao.sp.gov.br/MinhasTurmas/ConsultaAluno
```
