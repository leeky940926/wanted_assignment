안녕하세요.

위코드 25기로 이번 과정에 참여하게된 이기용입니다.

해당 README.md 파일은 구현한 API에 대한 설명을 표로 정리해서 만들었습니다.

각 API에 대해 표로 정리를 했으며, 구성은 HTTP Method / URI / Description / Request Variable / Response Status Code / Branch 입니다.

코드에 대한 추가 설명은 함께 제출한 PDF파일에 기술되어 있습니다.

읽어주셔서 감사합니다!

<br>

| Index  | Http Method |  URI            |  Description    |  Request variable  |  Response Status Code   | Branch
|:--------:|:-----------:|:----------------:|:----------------:|:----------------:|:----------------:|:------------------------:|
| 1 |  POST | /users/signup | 회원가입</br>(비밀번호 암호화,이메일과 </br>비밀번호 정규식</br>작성)  | email, password  | 201 | feature/signup
| 2 |  POST | /users/signin | 로그인(토큰 발행)  | email, password  | 201 | feature/signin
| 3 |  POST | /postings | 게시글 작성 | title, content, user_id</br>(유저 고유ID는 토큰으로</br>식별)  | 201 | feature/postings-c
| 4 |  GET | /postings | 게시글 조회</br>(offset과 limit을 </br>이용한 Pagination구현 | 없음  | 200 | feature/postings-r
| 5 |  PATCH | /postings/{posting_id} | 게시글 수정 | posting_id  | 201 | feature/postings-u
| 6 |  DELETE | /postings/{posting_id} | 게시글 삭제 | posting_id  | 201 | feature/postings-d

