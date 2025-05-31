CREATE SCHEMA IF NOT EXISTS "foon";


CREATE TABLE IF NOT EXISTS "foon"."fooninstances" ("id" INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                                                                             "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                                                                                            "record_source" TEXT NOT NULL);


CREATE TABLE IF NOT EXISTS "foon"."foondetectheartbeat" ("id" INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                                                                                   "heartbeat_time" TIMESTAMP NOT NULL,
                                                                                                                              "record_source" TEXT NOT NULL);