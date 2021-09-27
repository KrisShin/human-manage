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

 Date: 27/09/2021 17:25:09
*/


-- ----------------------------
-- Sequence structure for m_system_code_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."m_system_code_id_seq";
CREATE SEQUENCE "public"."m_system_code_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."m_system_code_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for m_user_info_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."m_user_info_id_seq";
CREATE SEQUENCE "public"."m_user_info_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "public"."m_user_info_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS "public"."alembic_version";
CREATE TABLE "public"."alembic_version" (
  "version_num" varchar(32) COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "public"."alembic_version" OWNER TO "postgres";

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
BEGIN;
INSERT INTO "public"."alembic_version" VALUES ('96edc2109d3c');
COMMIT;

-- ----------------------------
-- Table structure for m_department
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_department";
CREATE TABLE "public"."m_department" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "comment" text COLLATE "pg_catalog"."default",
  "dep_cd" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "dep_name" varchar(64) COLLATE "pg_catalog"."default",
  "factory_cd" varchar(2) COLLATE "pg_catalog"."default",
  "abort_div" int4
)
;
ALTER TABLE "public"."m_department" OWNER TO "postgres";

-- ----------------------------
-- Records of m_department
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_department" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, '010001', '人事部', '01', NULL);
INSERT INTO "public"."m_department" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, '010002', '销售部', '01', NULL);
INSERT INTO "public"."m_department" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, '020001', '财务部', '02', NULL);
COMMIT;

-- ----------------------------
-- Table structure for m_factory
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_factory";
CREATE TABLE "public"."m_factory" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "comment" text COLLATE "pg_catalog"."default",
  "factory_cd" varchar(2) COLLATE "pg_catalog"."default" NOT NULL,
  "factory_nm" varchar(64) COLLATE "pg_catalog"."default",
  "abort_div" int4
)
;
ALTER TABLE "public"."m_factory" OWNER TO "postgres";

-- ----------------------------
-- Records of m_factory
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_factory" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, '01', '食品厂', NULL);
INSERT INTO "public"."m_factory" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, '02', '服装厂', NULL);
COMMIT;

-- ----------------------------
-- Table structure for m_system_code
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_system_code";
CREATE TABLE "public"."m_system_code" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "comment" text COLLATE "pg_catalog"."default",
  "id" int4 NOT NULL DEFAULT nextval('m_system_code_id_seq'::regclass),
  "code_kbn" varchar(3) COLLATE "pg_catalog"."default",
  "code_kbn_nm" varchar(32) COLLATE "pg_catalog"."default",
  "code_no" varchar(3) COLLATE "pg_catalog"."default",
  "code_nm" varchar(32) COLLATE "pg_catalog"."default",
  "flug1" varchar(1) COLLATE "pg_catalog"."default",
  "flug1_nm" varchar(32) COLLATE "pg_catalog"."default",
  "flug2" varchar(1) COLLATE "pg_catalog"."default",
  "flug2_nm" varchar(10) COLLATE "pg_catalog"."default",
  "flug3" varchar(1) COLLATE "pg_catalog"."default",
  "flug3_nm" varchar(100) COLLATE "pg_catalog"."default",
  "factory_cd" varchar(2) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."m_system_code" OWNER TO "postgres";

-- ----------------------------
-- Records of m_system_code
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 1, '00', '廃止区分', '0', '使用（初期値）', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 2, '00', '廃止区分', '1', '停止', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 3, '00', '廃止区分', '2', '廃止', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 4, '01', '権限区分', '0', 'システム管理者', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 5, '01', '権限区分', '1', '管理者', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 6, '01', '権限区分', '2', '作業者', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 7, '02', '勤務形態', '1', '1勤（日勤）', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 8, '02', '勤務形態', '2', '2勤（夜勤）', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 9, '02', '勤務形態', '3', '全て', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 10, '03', '設備区分', '0', '全設備', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 11, '03', '設備区分', '1', '設備固有', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 12, '04', '設備メンテ区分', '1', '日常点検', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 13, '04', '設備メンテ区分', '2', '月末点検', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 14, '04', '設備メンテ区分', '3', '定期点検', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 15, '05', '設備イベントサイクル区分', '1', '稼働日全て', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 16, '05', '設備イベントサイクル区分', '2', '日付指定', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 17, '06', '工程種別区分', '1', '通常', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 18, '06', '工程種別区分', '2', '前工程', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 19, '07', '外注フラグ区分', '1', '社内', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 20, '07', '外注フラグ区分', '2', '社外', '2', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 21, '08', '作業者制約指定区分', '0', '指定無し（全作業者）', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 22, '08', '作業者制約指定区分', '1', '作業者指定', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 23, '09', '作業者イベント区分', '0', '朝礼', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 24, '09', '作業者イベント区分', '1', '午前', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 25, '09', '作業者イベント区分', '2', '午後', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 26, '09', '作業者イベント区分', '3', '定時休憩', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 27, '09', '作業者イベント区分', '4', '昼休み', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 28, '09', '作業者イベント区分', '5', '毎月祖先際', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 29, '09', '作業者イベント区分', '6', '休暇', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 30, '10', '品目ランク区分', '0', 'S', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 31, '10', '品目ランク区分', '1', 'A', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 32, '10', '品目ランク区分', '2', 'B', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 33, '10', '品目ランク区分', '3', 'C', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 34, '11', '品目別制約区分', '0', '条件なし', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 35, '11', '品目別制約区分', '1', '条件あり', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 36, '12', '作業区分', '0', 'ALL', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 37, '12', '作業区分', '1', '作業者', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 38, '12', '作業区分', '2', '設備', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 39, '12', '作業区分', '3', 'その他（待機）', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 40, '13', '休日区分', '0', '平日', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 41, '13', '休日区分', '1', '休日', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 42, '14', '月末区分', '1', '月末', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 43, '14', '月末区分', '0', 'その他', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 44, '15', 'カレンダー区分', '0', '全て', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 45, '15', 'カレンダー区分', '1', '作業者', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 46, '15', 'カレンダー区分', '2', '設備', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 47, '15', 'カレンダー区分', '3', 'その他', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 48, '16', '加工計画制約条件区分', '0', '条件なし', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 49, '16', '加工計画制約条件区分', '1', '作業者制約あり', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 50, '16', '加工計画制約条件区分', '2', '機械制約あり', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 51, '16', '加工計画制約条件区分', '3', '作業者、機械ともあり', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 52, '17', '作業者イベントサイクル区分', '0', '稼働日全て', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 53, '17', '作業者イベントサイクル区分', '1', '日付指定', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 54, '17', '作業者イベントサイクル区分', '2', '時間条件なし', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 55, '18', '確定コード区分', '0', '未確定', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 56, '18', '確定コード区分', '1', '確定', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 57, '19', '加工計画有無区分', '0', '計画なし', '1', '使用', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."m_system_code" VALUES (NULL, NULL, NULL, NULL, NULL, NULL, 58, '19', '加工計画有無区分', '1', '計画あり', '1', '使用', NULL, NULL, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for m_table_define
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_table_define";
CREATE TABLE "public"."m_table_define" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "class_name" varchar(64) COLLATE "pg_catalog"."default",
  "tbl_code" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "tbl_name" varchar(20) COLLATE "pg_catalog"."default",
  "field_code" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "field_name" varchar(20) COLLATE "pg_catalog"."default",
  "type" varchar(20) COLLATE "pg_catalog"."default",
  "size" varchar(20) COLLATE "pg_catalog"."default",
  "decimal" int4,
  "nullable" varchar(1) COLLATE "pg_catalog"."default",
  "doc" varchar(256) COLLATE "pg_catalog"."default",
  "comment" varchar(1024) COLLATE "pg_catalog"."default",
  "key" varchar(1) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."m_table_define" OWNER TO "postgres";

-- ----------------------------
-- Records of m_table_define
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:29:34.956959', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm5', '用户名5', 'DECIMAL', '5', 2, '1', '说明', '备注', NULL);
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:39:58.46814', NULL, 'demo_table1', 'demo_code1', 'demo1', 'user_nm5', '用户名5', 'DECIMAL', '5', 2, '1', '说明', '备注', '1');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:26:03.363814', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm2', '用户名2', 'DECIMAL', '5', 2, '0', '说明', '备注', NULL);
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:26:36.878737', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm3', '用户名3', 'DECIMAL', '5', 2, '0', '说明', '备注', NULL);
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:29:05.900317', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm4', '用户名4', 'DECIMAL', '5', 2, '0', '说明', '备注', NULL);
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:41:27.63727', NULL, 'demo_table2', 'demo_code2', 'demo2', 'user_nm3', '用户名3', 'DECIMAL', '5', 2, '0', '说明', '备注', '1');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:40:49.049555', NULL, 'demo_table1', 'demo_code1', 'demo1', 'user_nm4', '用户名4', 'DECIMAL', '5', 2, '0', '说明', '备注', '');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:41:05.013437', NULL, 'demo_table1', 'demo_code1', 'demo1', 'user_nm3', '用户名3', 'DECIMAL', '5', 2, '0', '说明', '备注', '');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:41:36.565933', NULL, 'demo_table2', 'demo_code2', 'demo2', 'user_nm1', '用户名1', 'DECIMAL', '5', 2, '1', '说明', '备注', '');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:22:59.615672', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm', '用户名', 'DECIMAL', '5', 2, '1', '说明', '备注', '1');
INSERT INTO "public"."m_table_define" VALUES (NULL, NULL, NULL, '2021-09-27 00:25:19.415989', NULL, 'demo_table', 'demo_code', 'demo', 'user_nm1', '用户名1', 'DECIMAL', '5', 2, '1', '说明', '备注', '1');
COMMIT;

-- ----------------------------
-- Table structure for m_user
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_user";
CREATE TABLE "public"."m_user" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "comment" text COLLATE "pg_catalog"."default",
  "user_cd" varchar(6) COLLATE "pg_catalog"."default" NOT NULL,
  "user_nm" varchar(64) COLLATE "pg_catalog"."default",
  "password" varchar(512) COLLATE "pg_catalog"."default",
  "create_user_id" varchar(6) COLLATE "pg_catalog"."default",
  "role_cd" int4,
  "duty_cd" int4,
  "abort_div" int4,
  "dep_cd" varchar(10) COLLATE "pg_catalog"."default",
  "factory_cd" varchar(2) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "public"."m_user" OWNER TO "postgres";

-- ----------------------------
-- Records of m_user
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_user" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:13.50034', NULL, NULL, '010001', 'testor', 'LBxZmYVrnG+Z+qC2xuTX/Q==
', NULL, 6, NULL, 1, NULL, '02');
INSERT INTO "public"."m_user" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:28.732013', NULL, NULL, '010002', 'testor', 'LBxZmYVrnG+Z+qC2xuTX/Q==
', NULL, 6, NULL, 1, NULL, '02');
INSERT INTO "public"."m_user" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:32.14875', NULL, NULL, '010003', 'testor', 'LBxZmYVrnG+Z+qC2xuTX/Q==
', NULL, 6, NULL, 1, NULL, '02');
INSERT INTO "public"."m_user" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:35.595719', NULL, NULL, '010004', 'testor', 'LBxZmYVrnG+Z+qC2xuTX/Q==
', NULL, 6, NULL, 1, NULL, '02');
COMMIT;

-- ----------------------------
-- Table structure for m_user_info
-- ----------------------------
DROP TABLE IF EXISTS "public"."m_user_info";
CREATE TABLE "public"."m_user_info" (
  "update_user_id" varchar(32) COLLATE "pg_catalog"."default",
  "update_count" int4,
  "update_pgid" varchar(512) COLLATE "pg_catalog"."default",
  "create_time" timestamp(6),
  "update_time" timestamp(6),
  "comment" text COLLATE "pg_catalog"."default",
  "id" int4 NOT NULL DEFAULT nextval('m_user_info_id_seq'::regclass),
  "name" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
  "sex" int4 NOT NULL,
  "birthday" timestamp(6),
  "phone" varchar(12) COLLATE "pg_catalog"."default" NOT NULL,
  "telephone" varchar(12) COLLATE "pg_catalog"."default",
  "email" varchar(128) COLLATE "pg_catalog"."default",
  "address1" varchar(256) COLLATE "pg_catalog"."default",
  "address2" varchar(256) COLLATE "pg_catalog"."default",
  "photo" varchar(1024) COLLATE "pg_catalog"."default",
  "factory_cd" varchar(2) COLLATE "pg_catalog"."default",
  "user_cd" varchar(6) COLLATE "pg_catalog"."default",
  "abort_div" int4
)
;
ALTER TABLE "public"."m_user_info" OWNER TO "postgres";

-- ----------------------------
-- Records of m_user_info
-- ----------------------------
BEGIN;
INSERT INTO "public"."m_user_info" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:13.518028', '2021-09-27 00:11:13.536745', NULL, 1, 'nicktest', 1, '1999-01-02 00:00:00', '13654987365', NULL, NULL, NULL, NULL, NULL, '02', '010001', NULL);
INSERT INTO "public"."m_user_info" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:28.742603', '2021-09-27 00:11:28.754921', NULL, 2, 'nicktest', 1, '1999-01-02 00:00:00', '13654987365', NULL, NULL, NULL, NULL, NULL, '02', '010002', NULL);
INSERT INTO "public"."m_user_info" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:32.159278', '2021-09-27 00:11:32.171863', NULL, 3, 'nicktest', 1, '1999-01-02 00:00:00', '13654987365', NULL, NULL, NULL, NULL, NULL, '02', '010003', NULL);
INSERT INTO "public"."m_user_info" VALUES (NULL, NULL, NULL, '2021-09-27 00:11:35.605392', '2021-09-27 00:11:35.61736', NULL, 4, 'nicktest', 1, '1999-01-02 00:00:00', '13654987365', NULL, NULL, NULL, NULL, NULL, '02', '010004', NULL);
COMMIT;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."m_system_code_id_seq"
OWNED BY "public"."m_system_code"."id";
SELECT setval('"public"."m_system_code_id_seq"', 60, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."m_user_info_id_seq"
OWNED BY "public"."m_user_info"."id";
SELECT setval('"public"."m_user_info_id_seq"', 6, true);

-- ----------------------------
-- Primary Key structure for table alembic_version
-- ----------------------------
ALTER TABLE "public"."alembic_version" ADD CONSTRAINT "alembic_version_pkc" PRIMARY KEY ("version_num");

-- ----------------------------
-- Indexes structure for table m_department
-- ----------------------------
CREATE INDEX "ix_m_department_factory_cd" ON "public"."m_department" USING btree (
  "factory_cd" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table m_department
-- ----------------------------
ALTER TABLE "public"."m_department" ADD CONSTRAINT "m_department_pkey" PRIMARY KEY ("dep_cd");

-- ----------------------------
-- Primary Key structure for table m_factory
-- ----------------------------
ALTER TABLE "public"."m_factory" ADD CONSTRAINT "m_factory_pkey" PRIMARY KEY ("factory_cd");

-- ----------------------------
-- Indexes structure for table m_system_code
-- ----------------------------
CREATE INDEX "ix_m_system_code_factory_cd" ON "public"."m_system_code" USING btree (
  "factory_cd" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table m_system_code
-- ----------------------------
ALTER TABLE "public"."m_system_code" ADD CONSTRAINT "unique_kbn_no" UNIQUE ("code_kbn", "code_no", "factory_cd");

-- ----------------------------
-- Primary Key structure for table m_system_code
-- ----------------------------
ALTER TABLE "public"."m_system_code" ADD CONSTRAINT "m_system_code_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table m_table_define
-- ----------------------------
ALTER TABLE "public"."m_table_define" ADD CONSTRAINT "m_table_define_pkey" PRIMARY KEY ("tbl_code", "field_code");

-- ----------------------------
-- Primary Key structure for table m_user
-- ----------------------------
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_pkey" PRIMARY KEY ("user_cd");

-- ----------------------------
-- Indexes structure for table m_user_info
-- ----------------------------
CREATE INDEX "ix_m_user_info_factory_cd" ON "public"."m_user_info" USING btree (
  "factory_cd" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "ix_m_user_info_id" ON "public"."m_user_info" USING btree (
  "id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "ix_m_user_info_sex" ON "public"."m_user_info" USING btree (
  "sex" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "ix_m_user_info_user_cd" ON "public"."m_user_info" USING btree (
  "user_cd" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table m_user_info
-- ----------------------------
ALTER TABLE "public"."m_user_info" ADD CONSTRAINT "m_user_info_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table m_department
-- ----------------------------
ALTER TABLE "public"."m_department" ADD CONSTRAINT "m_department_abort_div_fkey" FOREIGN KEY ("abort_div") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_department" ADD CONSTRAINT "m_department_factory_cd_fkey" FOREIGN KEY ("factory_cd") REFERENCES "public"."m_factory" ("factory_cd") ON DELETE CASCADE ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table m_factory
-- ----------------------------
ALTER TABLE "public"."m_factory" ADD CONSTRAINT "m_factory_abort_div_fkey" FOREIGN KEY ("abort_div") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table m_system_code
-- ----------------------------
ALTER TABLE "public"."m_system_code" ADD CONSTRAINT "m_system_code_factory_cd_fkey" FOREIGN KEY ("factory_cd") REFERENCES "public"."m_factory" ("factory_cd") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table m_user
-- ----------------------------
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_abort_div_fkey" FOREIGN KEY ("abort_div") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_dep_cd_fkey" FOREIGN KEY ("dep_cd") REFERENCES "public"."m_department" ("dep_cd") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_duty_cd_fkey" FOREIGN KEY ("duty_cd") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_factory_cd_fkey" FOREIGN KEY ("factory_cd") REFERENCES "public"."m_factory" ("factory_cd") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user" ADD CONSTRAINT "m_user_role_cd_fkey" FOREIGN KEY ("role_cd") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table m_user_info
-- ----------------------------
ALTER TABLE "public"."m_user_info" ADD CONSTRAINT "m_user_info_abort_div_fkey" FOREIGN KEY ("abort_div") REFERENCES "public"."m_system_code" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user_info" ADD CONSTRAINT "m_user_info_factory_cd_fkey" FOREIGN KEY ("factory_cd") REFERENCES "public"."m_factory" ("factory_cd") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."m_user_info" ADD CONSTRAINT "m_user_info_user_cd_fkey" FOREIGN KEY ("user_cd") REFERENCES "public"."m_user" ("user_cd") ON DELETE CASCADE ON UPDATE NO ACTION;
