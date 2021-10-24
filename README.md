| Index  | Http Method |  URI            |  Description    |  Request variable  |  Response Status Code   |
|:--------:|:-----------:|:----------------:|:----------------:|:----------------:|:----------------:|
| 1 |  POST | /users/signup | 회원가입(비밀번호 암호화, 이메일과 비밀번호 정규식 작성)  | email, password, phone_number, name  | 201
| 2 |  POST | /users/signin | 로그인(토큰 발행)  | email, password  | 201
| 3 |  POST | /postings | 게시글 작성 | title, content, user_id(유저 고유ID는 토큰으로 식별)  | 201
| 4 |  GET | /postings | 게시글 조회</br>(offset과 limit을 이용한 Pagination구현 | 없음  | 200
| 5 |  PATCH | /postings/{int:posting_id} | 게시글 수정 | posting_id  | 201
| 6 |  DELETE | /postings/{int:posting_id} | 게시글 삭제 | posting_id  | 201
