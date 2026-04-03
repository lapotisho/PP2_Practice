CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name TEXT,
    p_phone TEXT,
    p_email TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone, email = p_email
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone, email)
        VALUES (p_name, p_phone, p_email);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[],
    emails TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(names,1) != array_length(phones,1)
       OR array_length(names,1) != array_length(emails,1) THEN
        RAISE EXCEPTION 'Array lengths mismatch';
    END IF;

    FOR i IN 1..array_length(names, 1) LOOP
        
        IF phones[i] !~ '^\+77\d{9}$' THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];
        ELSE
            CALL upsert_contact(names[i], phones[i], emails[i]);
        END IF;

    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;