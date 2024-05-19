USE [trac_nghiem]
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'k4BYaYk7', N'teacher1@gmail.com', N'Đặng Hoài Phương', N'$2b$12$vRAvt7uiYPCmpf79FrzuAuXbO6yctv76uNhIa80i4vgzvVpUy4hQa', N'Teacher\k4BYaYk7\Avatar\k4BYaYk7.webp', 0, CAST(N'2024-04-09T21:23:09.543' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'LXZnq3cu', N'teacher4@gmail.com', N'Nguyễn Thị Lệ Quyên', N'$2b$12$RVObwuURD2yGrF7esrbEeOxgF7zlGDv9BdKJSZZ9K6jTZ7cHLSqQG', N'Teacher\LXZnq3cu\Avatar\LXZnq3cu.webp', 0, CAST(N'2024-05-19T22:34:49.220' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'qdj0IvKj', N'teacher3@gmail.com', N'Đặng Hoài Phương', N'$2b$12$7ykZao.Frb5AQ3oPTF8XA.27ScWuq0roZkR.YcJUn1vOwwskIuel2', NULL, 0, CAST(N'2024-04-11T19:00:16.653' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vHe3zIzf', N'teacher2@gmail.com', N'Võ Đức Hoàng', N'$2b$12$Gkph6kaLr6.Bi2WfjG/tuuDuL1apWsfV0Fa8nn3FYB.O/eaXZpNLC', NULL, 0, CAST(N'2024-04-11T19:00:04.087' AS DateTime), 0)
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'1tgJhUnW', N'k4BYaYk7', N'Tiếng Nhật 6', CAST(N'2024-04-27T11:08:26.297' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'41Y4GL7D', N'LXZnq3cu', N'Tiếng Nhật 2', CAST(N'2024-05-19T23:14:32.600' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'6d789LoC', N'k4BYaYk7', N'Lập trình python', CAST(N'2024-04-13T21:42:13.180' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'Alb7GgYY', N'LXZnq3cu', N'Tiếng Nhật 1', CAST(N'2024-05-19T23:14:24.903' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'kNEoTGIA', N'k4BYaYk7', N'Lập trình Java', CAST(N'2024-04-13T21:42:26.840' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'OeLujW1I', N'k4BYaYk7', N'Lập trình C#', CAST(N'2024-04-13T21:42:22.117' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'tSwFdgXT', N'k4BYaYk7', N'Lập trình mạng', CAST(N'2024-04-13T21:42:30.320' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'tw8NDxRE', N'LXZnq3cu', N'Tiếng Nhật 3', CAST(N'2024-05-19T23:14:46.167' AS DateTime))
GO
INSERT [dbo].[test] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'CxmFIKzP', N'Alb7GgYY', N'Giữa kỳ tiếng Nhật 1', CAST(N'2024-05-20T00:06:48.077' AS DateTime))
GO
INSERT [dbo].[test] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'jWMU08QZ', N'1tgJhUnW', N'Kiểm tra giữa kỳ tiếng Nhật 6', CAST(N'2024-05-15T23:08:51.897' AS DateTime))
GO
INSERT [dbo].[test] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'NnUesiqe', N'1tgJhUnW', N'Kiểm tra cuối tiếng Nhật 6', CAST(N'2024-05-17T16:18:28.497' AS DateTime))
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'1KyRhlne', N'Nhóm 21N11', N'LXZnq3cu', CAST(N'2024-05-19T22:44:05.490' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'4wFJBkca', N'GROUP 4', N'k4BYaYk7', CAST(N'2024-04-09T21:23:41.970' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'88lE7JMs', N'NHÓM 3', N'vHe3zIzf', CAST(N'2024-04-11T19:03:41.667' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'8KV9eD8t', N'GROUP 1', N'k4BYaYk7', CAST(N'2024-04-09T21:23:32.020' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'BfELboya', N'21N15', N'LXZnq3cu', CAST(N'2024-05-19T22:43:50.643' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'BWHlJddv', N'NHÓM 21.13', N'qdj0IvKj', CAST(N'2024-04-11T19:05:43.163' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'cdSUupLc', N'21TCLC_Nhat1', N'k4BYaYk7', CAST(N'2024-04-09T21:23:43.800' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'ch0RHd4F', N'GROUP 3', N'k4BYaYk7', CAST(N'2024-04-09T21:23:39.930' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'DiCEH2as', N'NHÓM 6', N'vHe3zIzf', CAST(N'2024-04-11T19:03:54.487' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'e73BTGJF', N'NHÓM 21.16', N'k4BYaYk7', CAST(N'2024-04-20T00:15:14.810' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'F4yxaXa2', N'NHÓM 5', N'vHe3zIzf', CAST(N'2024-04-11T19:03:46.793' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'H2hL5gmR', N'NHÓM 8', N'vHe3zIzf', CAST(N'2024-04-11T19:03:58.080' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'hJhx5jDm', N'NHÓM 2', N'vHe3zIzf', CAST(N'2024-04-11T19:03:39.230' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'jYITs8Rk', N'Nhóm 21N14', N'LXZnq3cu', CAST(N'2024-05-19T22:44:14.187' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'KTwfIxXF', N'NHÓM 7', N'vHe3zIzf', CAST(N'2024-04-11T19:03:56.277' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'm2UlagWs', N'Nhóm 21N12', N'LXZnq3cu', CAST(N'2024-05-19T22:44:08.543' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'MgbsLHP3', N'GROUP 9', N'k4BYaYk7', CAST(N'2024-04-09T21:23:53.343' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'mjuZ72rB', N'NHÓM 21.14', N'qdj0IvKj', CAST(N'2024-04-11T19:05:46.250' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'ohIym4EM', N'NHÓM 2', N'k4BYaYk7', CAST(N'2024-04-11T19:02:55.557' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'okwqEGLO', N'GROUP 10', N'k4BYaYk7', CAST(N'2024-04-09T21:23:57.223' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'PzZJoaTL', N'GROUP 6', N'k4BYaYk7', CAST(N'2024-04-09T21:23:46.017' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'QgB3WvKg', N'GROUP 2', N'k4BYaYk7', CAST(N'2024-04-09T21:23:37.807' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'qJyDN6Nj', N'NHÓM 21.12', N'qdj0IvKj', CAST(N'2024-04-11T19:05:38.470' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'QsAfNNGN', N'Nhóm 21N13', N'LXZnq3cu', CAST(N'2024-05-19T22:44:11.163' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'tqiOBYQR', N'GROUP 7', N'k4BYaYk7', CAST(N'2024-04-09T21:23:47.683' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'tU7Z7LzW', N'NHÓM 3', N'k4BYaYk7', CAST(N'2024-04-11T19:02:57.997' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'uxpWkXSK', N'NHÓM 4', N'vHe3zIzf', CAST(N'2024-04-11T19:03:44.290' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'uzKPouin', N'NHÓM 1', N'k4BYaYk7', CAST(N'2024-04-11T19:02:52.893' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'vKKOhuV5', N'NHÓM 21.16', N'qdj0IvKj', CAST(N'2024-04-11T19:05:56.537' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'X7DytzIM', N'NHÓM 21.15', N'qdj0IvKj', CAST(N'2024-04-11T19:05:49.610' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'yzzd7zkN', N'GROUP 8', N'k4BYaYk7', CAST(N'2024-04-09T21:23:49.953' AS DateTime), 0, NULL)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show], [image_path]) VALUES (N'ZR9t9Jjv', N'NHÓM 1', N'vHe3zIzf', CAST(N'2024-04-11T19:03:36.220' AS DateTime), 1, NULL)
GO
INSERT [dbo].[group_test] ([id], [group_id], [test_id], [start], [end], [created_timestamp], [duration], [shuffle], [name]) VALUES (N'5ramLUdO', N'uzKPouin', N'jWMU08QZ', CAST(N'2024-05-13T09:30:00.000' AS DateTime), CAST(N'2024-05-18T11:30:00.000' AS DateTime), CAST(N'2024-05-15T23:09:27.603' AS DateTime), 100, 1, NULL)
GO
INSERT [dbo].[group_test] ([id], [group_id], [test_id], [start], [end], [created_timestamp], [duration], [shuffle], [name]) VALUES (N'ydBokRde', N'1KyRhlne', N'CxmFIKzP', CAST(N'2024-05-15T09:30:00.000' AS DateTime), CAST(N'2024-05-25T11:30:00.000' AS DateTime), CAST(N'2024-05-20T00:09:30.107' AS DateTime), 100, 0, N'Kiểm tra giữa kỳ tiếng Nhật 6')
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'AF2VbKXC', N'Alb7GgYY', N'Ngữ pháp N5', CAST(N'2024-05-19T23:17:53.067' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'cc2Gwojy', N'1tgJhUnW', N'Đọc hiểu N3', CAST(N'2024-04-27T11:09:23.600' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'e77fmDUK', N'Alb7GgYY', N'Đọc hiểu N5', CAST(N'2024-05-19T23:18:13.413' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'Ff2II1ZI', N'1tgJhUnW', N'Nghe hiểu N3', CAST(N'2024-04-27T11:09:28.900' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'GT1eAE3b', N'Alb7GgYY', N'Hán tự N5', CAST(N'2024-05-19T23:18:08.950' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'JRlaw4RT', N'1tgJhUnW', N'Hán tự N3', CAST(N'2024-04-27T11:09:18.440' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'kCBCsMVA', N'Alb7GgYY', N'Từ vựng N5', CAST(N'2024-05-19T23:18:04.723' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'TaOqAVbD', N'1tgJhUnW', N'Từ vựng N3', CAST(N'2024-04-27T11:09:08.647' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'XyHSTRRM', N'Alb7GgYY', N'Nghe hiểu N5', CAST(N'2024-05-19T23:18:19.267' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'Ye5fT2tZ', N'1tgJhUnW', N'Ngữ pháp N3', CAST(N'2024-05-13T19:59:16.340' AS DateTime))
GO
INSERT [dbo].[test_structure] ([test_id], [question_bank_id], [number_of_question]) VALUES (N'CxmFIKzP', N'kCBCsMVA', 0x80049585000000000000005D94288C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C104E756D6265724F665175657374696F6E9493942981947D94288C0A646966666963756C7479944B018C126E756D6265725F6F665F7175657374696F6E944B02756268032981947D942868064B0268074B02756268032981947D942868064B0368074B017562652E)
GO
INSERT [dbo].[test_structure] ([test_id], [question_bank_id], [number_of_question]) VALUES (N'CxmFIKzP', N'XyHSTRRM', 0x80049560000000000000005D948C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C104E756D6265724F665175657374696F6E9493942981947D94288C0A646966666963756C7479944B018C126E756D6265725F6F665F7175657374696F6E944B027562612E)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'8iOZNT4P', N'student1@gmail.com', N'Goku', N'$2b$12$iysRFi8UcisVI.zZu0XT9eJJwCWuGaLlid0HdRxOnVinjC6Rwd8Pe', N'Student\8iOZNT4P\Avatar\8iOZNT4P.webp', 0, CAST(N'2024-04-09T21:24:09.537' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'KNJLbbTP', N'student11@gmail.com', N'Nguyễn Đức Chung', N'$2b$12$Zt2ODbX15JUkV5EtS3y8x.spkVO/3Xqspm0jkxl/9SbB1HsLvJcI2', N'Student\KNJLbbTP\Avatar\KNJLbbTP.jpg', 0, CAST(N'2024-05-19T22:39:45.750' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'NkvFWLYJ', N'student8@gmail.com', N'Học sinh 8', N'$2b$12$AF8n2CDmzTKOlt6DdzPC2uVIxGud9H4H4Y3oQIobw/Jecq5mZRs4O', NULL, 0, CAST(N'2024-04-09T21:24:40.797' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'olF2PEiv', N'student4@gmail.com', N'Học sinh 4', N'$2b$12$lTEG7fcENFpnDsv9Tvc8luDkH8MiDHVARWE4u8c2pIXqqpbRYzQoK', NULL, 0, CAST(N'2024-04-09T21:24:22.130' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'qVcy54uO', N'student5@gmail.com', N'Học sinh 5', N'$2b$12$oQa66pl6RkFo2q4bMT6FludvgxaAsfyUZf72vFRxH3YQhxB74YgDG', NULL, 0, CAST(N'2024-04-09T21:24:26.060' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'SlW241eT', N'student9@gmail.com', N'Học sinh 9', N'$2b$12$rmzWumCZ/FGXeDyaTYpNueX5mmzb3VCoeTCfcM0puD3Z4eXOjB26q', NULL, 0, CAST(N'2024-04-09T21:24:45.250' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'Tj2WdsIk', N'student10@gmail.com', N'Học sinh 10', N'$2b$12$/ncUjvvpPOllKU9dB/9KZe7Bc9VPIsI3ziLQ5dw16b0BxYRRmBO0W', NULL, 0, CAST(N'2024-04-09T21:24:51.960' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vAN0Ef2M', N'student6@gmail.com', N'Học sinh 6', N'$2b$12$4foUvTAjgSuILq/wd9ffdekuUh7YOB3.ZTm24rz9Gw2xMrPu4Gl2O', NULL, 0, CAST(N'2024-04-09T21:24:31.320' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'VoJY8oV3', N'student2@gmail.com', N'Học sinh 2', N'$2b$12$pEvbcDxT6G.dV1Qpwb.7X.xfr3SsTBRLBX2Xeo0CWeYNQ8jeP54CW', NULL, 0, CAST(N'2024-04-09T21:24:13.717' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vwRhDHHL', N'student3@gmail.com', N'Học sinh 3', N'$2b$12$65v2uH4mVXvNTFcyi38zuOYGzXt8JXcy9dwSD9BenHP/E97o15K0W', NULL, 0, CAST(N'2024-04-09T21:24:17.667' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'Z7cJJrs1', N'student7@gmail.com', N'Học sinh 7', N'$2b$12$ZEhH2eHFlH9MYSGdc3CIfucb.dPgQT9Uf3G6t4kaMEmaw6In/YqSe', NULL, 0, CAST(N'2024-04-09T21:24:35.977' AS DateTime), 0)
GO
INSERT [dbo].[student_test] ([student_id], [group_test_id], [start], [end], [student_work], [score]) VALUES (N'KNJLbbTP', N'ydBokRde', CAST(N'2024-05-20T00:11:47.677' AS DateTime), CAST(N'2024-05-20T00:23:30.307' AS DateTime), 0x80049593030000000000005D94288C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C1453747564656E74576F726B5F5175657374696F6E9493942981947D94288C07636F6E74656E74948C06E4BD9CE3828B948C06616E737765729468018C06416E737765729493942981947D94288C0474657874945D94288C09E381A4E3818FE3828B948C09E38199E3818FE3828B948C09E38280E38199E3818F948C09E38186E381A4E3828B94658C07636F7272656374948F94284B009075628C0A6174746163686D656E74944E8C0E73747564656E745F616E73776572945D944B0061756268032981947D942868068C03E99BA8946808680A2981947D9428680D5D94288C06E381ABE3818F948C06E38182E38281948C06E381B5E38286948C06E38182E3818D946568138F94284B0190756268154E68165D944B0161756268032981947D942868068C06E9BCBBE6B0B4946808680A2981947D9428680D5D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B3946568138F94284B0290756268154E68165D944B0261756268032981947D942868068C06E9BCBBE6B0B4946808680A2981947D9428680D5D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B3946568138F94284B0290756268154E68165D944B0261756268032981947D942868068C06E5A4A7E5A489946808680A2981947D9428680D5D94288C12E381A0E38184E38198E38287E38186E381B6948C0CE381B8E38293E3819FE38184948C06E381B8E38293948C0CE3819FE38184E381B8E38293946568138F94284B0390756268154E68165D944B0361756268032981947D942868068C00946808680A2981947D9428680D5D94288C12E38199E38190E5AEB6E381ABE5B8B0E3828B948C1BE382AFE383A9E382B9E38292E58F97E38191E381A6E381BFE3828B948C1EE382AFE383A9E382B9E38292E8A68BE5ADA6E38197E381A6E381BFE3828B948C24E382AFE383A9E382B9E381ABE585A5E3828BE6898BE7B69AE3818DE38292E38199E3828B946568138F94284B0290756268154E68165D944B0161756268032981947D94286806684A6808680A2981947D9428680D5D94288C03E382A2948C06E382A2E382A4948C06E382A4E382A6948C06E382A2E382A6946568138F94284B0190756268154E68165D944B00617562652E, 0.7142857142857143)
GO
INSERT [dbo].[student_test] ([student_id], [group_test_id], [start], [end], [student_work], [score]) VALUES (N'VoJY8oV3', N'ydBokRde', CAST(N'2024-05-20T00:29:52.310' AS DateTime), CAST(N'2024-05-20T00:30:33.603' AS DateTime), 0x80049593030000000000005D94288C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C1453747564656E74576F726B5F5175657374696F6E9493942981947D94288C07636F6E74656E74948C06E4BD9CE3828B948C06616E737765729468018C06416E737765729493942981947D94288C0474657874945D94288C09E381A4E3818FE3828B948C09E38199E3818FE3828B948C09E38280E38199E3818F948C09E38186E381A4E3828B94658C07636F7272656374948F94284B009075628C0A6174746163686D656E74944E8C0E73747564656E745F616E73776572945D944B0061756268032981947D942868068C03E99BA8946808680A2981947D9428680D5D94288C06E381ABE3818F948C06E38182E38281948C06E381B5E38286948C06E38182E3818D946568138F94284B0190756268154E68165D944B0161756268032981947D942868068C06E9BCBBE6B0B4946808680A2981947D9428680D5D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B3946568138F94284B0290756268154E68165D944B0261756268032981947D942868068C06E9BCBBE6B0B4946808680A2981947D9428680D5D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B3946568138F94284B0290756268154E68165D944B0261756268032981947D942868068C06E5A4A7E5A489946808680A2981947D9428680D5D94288C12E381A0E38184E38198E38287E38186E381B6948C0CE381B8E38293E3819FE38184948C06E381B8E38293948C0CE3819FE38184E381B8E38293946568138F94284B0390756268154E68165D944B0361756268032981947D942868068C00946808680A2981947D9428680D5D94288C12E38199E38190E5AEB6E381ABE5B8B0E3828B948C1BE382AFE383A9E382B9E38292E58F97E38191E381A6E381BFE3828B948C1EE382AFE383A9E382B9E38292E8A68BE5ADA6E38197E381A6E381BFE3828B948C24E382AFE383A9E382B9E381ABE585A5E3828BE6898BE7B69AE3818DE38292E38199E3828B946568138F94284B0290756268154E68165D944B0261756268032981947D94286806684A6808680A2981947D9428680D5D94288C03E382A2948C06E382A2E382A4948C06E382A4E382A6948C06E382A2E382A6946568138F94284B0190756268154E68165D944B01617562652E, 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'8iOZNT4P', 1, CAST(N'2024-05-19T22:58:55.717' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'KNJLbbTP', 1, CAST(N'2024-05-19T22:47:57.033' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'olF2PEiv', 1, CAST(N'2024-05-19T22:57:29.943' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'Tj2WdsIk', 1, CAST(N'2024-05-19T22:47:57.033' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'VoJY8oV3', 1, CAST(N'2024-05-19T22:59:03.653' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'1KyRhlne', N'vwRhDHHL', 1, CAST(N'2024-05-19T22:59:03.657' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'8iOZNT4P', 1, CAST(N'2024-04-12T17:30:21.940' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'NkvFWLYJ', 1, CAST(N'2024-04-12T17:30:21.963' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'olF2PEiv', 1, CAST(N'2024-04-12T17:30:21.987' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'VoJY8oV3', 1, CAST(N'2024-05-16T22:47:02.597' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'vwRhDHHL', 1, CAST(N'2024-05-16T22:47:02.597' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'88lE7JMs', N'8iOZNT4P', 1, CAST(N'2024-04-11T20:04:38.593' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'88lE7JMs', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.850' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'BfELboya', N'KNJLbbTP', 1, CAST(N'2024-05-19T23:01:36.253' AS DateTime), 0)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:40:56.223' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'olF2PEiv', 0, CAST(N'2024-04-11T20:40:56.230' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'qVcy54uO', 0, CAST(N'2024-04-11T20:40:56.230' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'SlW241eT', 0, CAST(N'2024-04-11T20:40:56.237' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'Tj2WdsIk', 0, CAST(N'2024-04-11T20:40:56.240' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'DiCEH2as', N'8iOZNT4P', 1, CAST(N'2024-04-11T20:04:47.683' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'DiCEH2as', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.860' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'F4yxaXa2', N'8iOZNT4P', 0, CAST(N'2024-04-11T20:04:51.653' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'F4yxaXa2', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.863' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'H2hL5gmR', N'8iOZNT4P', 0, CAST(N'2024-04-11T20:04:57.803' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'H2hL5gmR', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.867' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'vKKOhuV5', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.870' AS DateTime), 1)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'b3cM3cQLZV', N'XyHSTRRM', -32768, N'', 0x800495C3000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C12E38199E38190E5AEB6E381ABE5B8B0E3828B948C1BE382AFE383A9E382B9E38292E58F97E38191E381A6E381BFE3828B948C1EE382AFE383A9E382B9E38292E8A68BE5ADA6E38197E381A6E381BFE3828B948C24E382AFE383A9E382B9E381ABE585A5E3828BE6898BE7B69AE3818DE38292E38199E3828B94658C07636F7272656374948F94284B029075622E, 1, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'bCqutM2RHj', N'kCBCsMVA', -32768, N'作る', 0x80049578000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C09E381A4E3818FE3828B948C09E38199E3818FE3828B948C09E38280E38199E3818F948C09E38186E381A4E3828B94658C07636F7272656374948F94284B009075622E, 1, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'GiGMYesZUE', N'kCBCsMVA', -32764, N'大変', 0x80049584000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C12E381A0E38184E38198E38287E38186E381B6948C0CE381B8E38293E3819FE38184948C06E381B8E38293948C0CE3819FE38184E381B8E3829394658C07636F7272656374948F94284B039075622E, 3, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'JvdPT2KPj6', N'kCBCsMVA', -32766, N'鼻水', 0x80049581000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B394658C07636F7272656374948F94284B029075622E, 2, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'mladzPgda2', N'kCBCsMVA', -32767, N'雨', 0x8004956C000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C06E381ABE3818F948C06E38182E38281948C06E381B5E38286948C06E38182E3818D94658C07636F7272656374948F94284B019075622E, 1, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'Nh5PaFiwhL', N'kCBCsMVA', -32765, N'鼻水', 0x80049581000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C0CE381A1E3818DE3819FE3818B948C0CE381B2E381B2E381AFE381AF948C0CE381AFE381AAE381BFE3819A948C09E381AFE381AAE381B394658C07636F7272656374948F94284B029075622E, 2, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'ubmeF9LOCb', N'XyHSTRRM', -32767, N'', 0x80049569000000000000008C164261636B656E642E4D6F64656C2E44425F6D6F64656C948C06416E737765729493942981947D94288C0474657874945D94288C03E382A2948C06E382A2E382A4948C06E382A4E382A6948C06E382A2E382A694658C07636F7272656374948F94284B019075622E, 1, NULL)
GO
