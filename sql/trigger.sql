-- [admin]
CREATE TRIGGER generate_admin_id
ON [admin]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [admin] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [admin] ([id], [username], [hash_pswd], [name], [is_banned])
      SELECT @new_id, [username], [hash_pswd], [name], [is_banned]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [student]
CREATE TRIGGER generate_student_id
ON [student]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [student] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned])
      SELECT @new_id, [email], [name], [hash_pswd], [avatar_path], [is_banned]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [teacher]
CREATE TRIGGER generate_teacher_id
ON [teacher]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [teacher] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned])
      SELECT @new_id, [email], [name], [hash_pswd], [avatar_path], [is_banned]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [group]
CREATE TRIGGER generate_group_id
ON [group]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [group] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [group] ([id], [name], [teacher_id], [created_timestamp], [is_show])
      SELECT @new_id, [name], [teacher_id], [created_timestamp], [is_show]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [group_test]
CREATE TRIGGER generate_group_test_id
ON [group_test]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [group_test] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [group_test] ([id], [group_id], [test_path], [start], [end], [created_timestamp])
      SELECT @new_id, [group_id], [test_path], [start], [end], [created_timestamp]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [collection]
CREATE TRIGGER generate_collection_id
ON [collection]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [collection] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [collection] ([id], [teacher_id], [name])
      SELECT @new_id, [teacher_id], [name]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [question_bank]
CREATE TRIGGER generate_question_bank_id
ON [question_bank]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [question_bank] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [question_bank] ([id], [collection_id], [name])
      SELECT @new_id, [collection_id], [name]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [generate_test]
CREATE TRIGGER generate_generate_test_id
ON [generate_test]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [generate_test] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [generate_test] ([id], [collection_id], [name])
      SELECT @new_id, [collection_id], [name]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO

-- [manual_test]
CREATE TRIGGER generate_manual_test_id
ON [manual_test]
INSTEAD OF INSERT
AS
BEGIN
  DECLARE @new_id AS VARCHAR(8);
  DECLARE @attempt AS INT = 0;

  WHILE @attempt < 100
  BEGIN
    SET @new_id = LEFT(NEWID(), 8);

    IF NOT EXISTS (SELECT * FROM [manual_test] WHERE [id] = @new_id)
    BEGIN
      INSERT INTO [manual_test] ([id], [collection_id], [name])
      SELECT @new_id, [collection_id], [name]
      FROM inserted;
      BREAK;
    END

    SET @attempt += 1;
  END

  IF @attempt >= 100
  BEGIN
    RAISERROR ('Failed to generate unique ID after 100 attempts', 16, 1);
  END
END
GO