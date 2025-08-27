/*
 Navicat Premium Data Transfer

 Source Server         : 香港华为数据库
 Source Server Type    : MySQL
 Source Server Version : 80041 (8.0.41-0ubuntu0.22.04.1)
 Source Host           : 119.8.121.24:3306
 Source Schema         : spider_data

 Target Server Type    : MySQL
 Target Server Version : 80041 (8.0.41-0ubuntu0.22.04.1)
 File Encoding         : 65001

 Date: 26/08/2025 15:37:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for document
-- ----------------------------
DROP TABLE IF EXISTS `document`;
CREATE TABLE `document`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '采集表名字',
  `table_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '数据存储表名',
  `count` bigint NOT NULL DEFAULT 0 COMMENT '采集数据总数',
  `comment` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL COMMENT '备注',
  `source` int NOT NULL COMMENT '任务来源（任务ID）',
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_table_name`(`table_name` ASC) USING BTREE,
  INDEX `idx_source`(`source` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '文档表（数据采集汇总表）' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of document
-- ----------------------------
INSERT INTO `document` VALUES (1, '科技厅通知', 'kjt_tz', 0, '科技厅通知', 1, '2025-08-24 09:52:34.008366', '2025-08-26 15:00:19.341338');
INSERT INTO `document` VALUES (2, '随机采集演示', 'bilibili_test', 2800, '随机视频推荐信息采集', 2, '2025-08-24 09:52:34.008366', '2025-08-26 15:00:43.446790');
INSERT INTO `document` VALUES (3, '交通部信息公开', 'mot_xxgk2', 728, '交通部信息公开', 604, '2025-08-26 15:14:10.000000', '2025-08-26 15:09:39.406633');
INSERT INTO `document` VALUES (4, '应急厅行政文件', 'yjt_xzwj', 466, '应急厅形政规范文件', 496, '2025-08-26 10:08:06.000000', '2025-08-26 15:16:57.576235');
INSERT INTO `document` VALUES (5, '应急厅政策解读', 'yjt_zcjd', 177, '应急厅政策解读', 239, '2025-08-26 22:44:25.000000', '2025-08-26 15:21:28.261204');

SET FOREIGN_KEY_CHECKS = 1;
