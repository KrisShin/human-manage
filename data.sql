/*
 Navicat Premium Data Transfer

 Source Server         : local_pg
 Source Server Type    : PostgreSQL
 Source Server Version : 130004
 Source Host           : localhost:35432
 Source Catalog        : humanmanage
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 130004
 File Encoding         : 65001

 Date: 31/08/2021 11:58:19
*/


-- ----------------------------
-- Sequence structure for tb_department_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_department_id_seq";
CREATE SEQUENCE "public"."tb_department_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."tb_department_id_seq" OWNER TO "humanuser";

-- ----------------------------
-- Sequence structure for tb_menu_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_menu_id_seq";
CREATE SEQUENCE "public"."tb_menu_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."tb_menu_id_seq" OWNER TO "humanuser";

-- ----------------------------
-- Sequence structure for tb_users_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tb_users_id_seq";
CREATE SEQUENCE "public"."tb_users_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."tb_users_id_seq" OWNER TO "humanuser";

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS "public"."alembic_version";
CREATE TABLE "public"."alembic_version" (
  "version_num" varchar(32) COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "public"."alembic_version" OWNER TO "humanuser";

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
BEGIN;
INSERT INTO "public"."alembic_version" VALUES ('85ee87746147');
COMMIT;

-- ----------------------------
-- Table structure for tb_department
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_department";
CREATE TABLE "public"."tb_department" (
  "id" int4 NOT NULL DEFAULT nextval('tb_department_id_seq'::regclass),
  "name" varchar(64) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."tb_department" OWNER TO "humanuser";

-- ----------------------------
-- Records of tb_department
-- ----------------------------
BEGIN;
INSERT INTO "public"."tb_department" VALUES (1, '财务部');
INSERT INTO "public"."tb_department" VALUES (2, '采购部');
INSERT INTO "public"."tb_department" VALUES (3, '营销部');
INSERT INTO "public"."tb_department" VALUES (4, '开发部');
INSERT INTO "public"."tb_department" VALUES (5, '售后部');
INSERT INTO "public"."tb_department" VALUES (6, '人事部');
INSERT INTO "public"."tb_department" VALUES (7, '保卫部');
INSERT INTO "public"."tb_department" VALUES (8, '小卖部');
COMMIT;

-- ----------------------------
-- Table structure for tb_menu
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_menu";
CREATE TABLE "public"."tb_menu" (
  "id" int4 NOT NULL DEFAULT nextval('tb_menu_id_seq'::regclass),
  "name" varchar(64) COLLATE "pg_catalog"."default",
  "level" int4,
  "parent" int4,
  "path" varchar(256) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."tb_menu" OWNER TO "humanuser";

-- ----------------------------
-- Records of tb_menu
-- ----------------------------
BEGIN;
INSERT INTO "public"."tb_menu" VALUES (1, '基础数据', 0, NULL, '/base');
INSERT INTO "public"."tb_menu" VALUES (2, '人员信息', 1, 1, '/base/humanInfo');
INSERT INTO "public"."tb_menu" VALUES (3, '部门信息', 1, 1, '/base/departmentInfo');
INSERT INTO "public"."tb_menu" VALUES (4, '公司信息', 1, 1, '/base/companyInfo');
INSERT INTO "public"."tb_menu" VALUES (5, '业务数据', 0, NULL, '/data');
INSERT INTO "public"."tb_menu" VALUES (6, '社内业务', 1, 5, '/data/Internal');
INSERT INTO "public"."tb_menu" VALUES (7, '社外业务', 1, 5, '/data/external');
INSERT INTO "public"."tb_menu" VALUES (8, '其他业务', 1, 5, '/data/other');
COMMIT;

-- ----------------------------
-- Table structure for tb_users
-- ----------------------------
DROP TABLE IF EXISTS "public"."tb_users";
CREATE TABLE "public"."tb_users" (
  "id" int4 NOT NULL DEFAULT nextval('tb_users_id_seq'::regclass),
  "name" varchar(64) COLLATE "pg_catalog"."default",
  "email" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "password" varchar(1024) COLLATE "pg_catalog"."default",
  "position" varchar(512) COLLATE "pg_catalog"."default",
  "office" varchar(512) COLLATE "pg_catalog"."default",
  "salary" float8,
  "status" varchar(64) COLLATE "pg_catalog"."default",
  "department_id" int4,
  "gender" varchar(2) COLLATE "pg_catalog"."default",
  "age" int4
)
;
ALTER TABLE "public"."tb_users" OWNER TO "humanuser";

-- ----------------------------
-- Records of tb_users
-- ----------------------------
BEGIN;
INSERT INTO "public"."tb_users" VALUES (14, 'gayQdURsB', 'qNIidQdY@uWsLcW.com', '2021-09-26 15:51:04.780929', NULL, 'cb59e849db164afdff0be42c9c546716', 'vNbCnyMKIV', 'jFxPHWUzjh', 70858, '在职', 1, '男', 23);
INSERT INTO "public"."tb_users" VALUES (1, '刘德华', 'dehua.liu@humanmanage.com', '2021-08-26 15:13:50.921226', NULL, 'cb59e849db164afdff0be42c9c546716', '前端开发', '上海', 15000, '在职', 1, '男', 35);
INSERT INTO "public"."tb_users" VALUES (6, 'PsomXek', 'mnziUti@eGMhhox.com', '2021-08-26 15:51:04.737983', NULL, 'cb59e849db164afdff0be42c9c546716', 'uAEUEdAUl', 'jwrQZc', 40203, '在职', 6, '男', 37);
INSERT INTO "public"."tb_users" VALUES (5, 'CocmsKh', 'sMKjTikh@NqOQjaRK.com', '2021-08-26 15:51:04.701423', NULL, 'cb59e849db164afdff0be42c9c546716', 'LCjRjkj', 'bbDYN', 139133, '休假', 6, '男', 26);
INSERT INTO "public"."tb_users" VALUES (2, '马德华', 'dehua.ma@humanmanage.com', '2021-08-26 15:16:43.712553', NULL, 'cb59e849db164afdff0be42c9c546716', 'Java开发', '成都', 18000, '在职', NULL, '男', 45);
INSERT INTO "public"."tb_users" VALUES (3, '张学友', 'xueyou.zhang@humanmanage.com', '2021-08-26 15:17:45.96305', NULL, 'cb59e849db164afdff0be42c9c546716', '保洁', '天津', 8000, '休假', 1, '男', 43);
INSERT INTO "public"."tb_users" VALUES (7, 'BcZPHglEZ', 'JqaVWAHKGd@DnFfH.com', '2021-08-30 15:51:04.74774', NULL, 'cb59e849db164afdff0be42c9c546716', 'lvMFllhHrJ', 'ZWFrBqa', 119884, '在职', 4, '男', 37);
INSERT INTO "public"."tb_users" VALUES (8, 'kOxxmYXDeN', 'UnhmbGSbO@BkadoQhWY.com', '2021-08-30 15:51:04.74774', NULL, 'cb59e849db164afdff0be42c9c546716', 'JdTjhxUm', 'iTIABixj', 103772, '在职', 8, '女', 32);
INSERT INTO "public"."tb_users" VALUES (10, 'hzFGgKN', 'oquvVHBRKa@jAiGzMus.com', '2021-08-30 15:51:04.74774', NULL, 'cb59e849db164afdff0be42c9c546716', 'rOUsbBBP', 'SEhVEdeV', 179399, '在职', 5, '女', 29);
INSERT INTO "public"."tb_users" VALUES (9, 'lEdrVCmah', 'UwjmU@DeDPbKAuH.com', '2021-08-30 15:51:04.74774', NULL, 'cb59e849db164afdff0be42c9c546716', 'htLmQ', 'xwQmEU', 184634, '在职', 1, '女', 29);
INSERT INTO "public"."tb_users" VALUES (11, 'CeXImx', 'UtYdrnrorQ@oBfCx.com', '2021-08-30 15:51:04.74774', NULL, 'cb59e849db164afdff0be42c9c546716', 'mnfGjNGYhg', 'eamZLju', 133264, '在职', 1, '女', 26);
INSERT INTO "public"."tb_users" VALUES (12, 'LrUQeOcTh', 'SFZDycyF@MyMaUCQvpB.com', '2021-09-26 15:51:04.780929', NULL, 'cb59e849db164afdff0be42c9c546716', 'EELGVvC', 'ngfAOWCYPH', 104123, '在职', 6, '女', 30);
INSERT INTO "public"."tb_users" VALUES (13, 'xatnOLU', 'ZBGGC@jLtYbJZwu.com', '2021-09-26 15:51:04.780929', NULL, 'cb59e849db164afdff0be42c9c546716', 'sDzbnxhkH', 'HrCqG', 62536, '在职', 2, '女', 33);
COMMIT;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_department_id_seq"
OWNED BY "public"."tb_department"."id";
SELECT setval('"public"."tb_department_id_seq"', 12, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_menu_id_seq"
OWNED BY "public"."tb_menu"."id";
SELECT setval('"public"."tb_menu_id_seq"', 12, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tb_users_id_seq"
OWNED BY "public"."tb_users"."id";
SELECT setval('"public"."tb_users_id_seq"', 18, true);

-- ----------------------------
-- Primary Key structure for table alembic_version
-- ----------------------------
ALTER TABLE "public"."alembic_version" ADD CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num");

-- ----------------------------
-- Indexes structure for table tb_department
-- ----------------------------
CREATE INDEX "ix_tb_department_id" ON "public"."tb_department" USING btree (
  "id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table tb_department
-- ----------------------------
ALTER TABLE "public"."tb_department" ADD CONSTRAINT "tb_department_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table tb_menu
-- ----------------------------
CREATE INDEX "ix_tb_menu_id" ON "public"."tb_menu" USING btree (
  "id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table tb_menu
-- ----------------------------
ALTER TABLE "public"."tb_menu" ADD CONSTRAINT "tb_menu_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table tb_users
-- ----------------------------
CREATE INDEX "ix_tb_users_department_id" ON "public"."tb_users" USING btree (
  "department_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "ix_tb_users_id" ON "public"."tb_users" USING btree (
  "id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table tb_users
-- ----------------------------
ALTER TABLE "public"."tb_users" ADD CONSTRAINT "tb_users_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table tb_users
-- ----------------------------
ALTER TABLE "public"."tb_users" ADD CONSTRAINT "tb_users_department_id_fkey" FOREIGN KEY ("department_id") REFERENCES "public"."tb_department" ("id") ON DELETE CASCADE ON UPDATE NO ACTION;
