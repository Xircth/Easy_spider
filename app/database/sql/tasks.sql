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

 Date: 26/08/2025 15:37:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tasks
-- ----------------------------
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `task_id` int NOT NULL COMMENT '任务ID，表示一种类型的任务',
  `task_E_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '任务执行ID，表示任务执行的唯一标识',
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'pending' COMMENT '任务状态（pending, running, stop, finished）',
  `created_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '任务创建时间',
  `finish_time` datetime(6) NULL DEFAULT NULL COMMENT '任务完成或终止时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_task_E_id`(`task_E_id` ASC) USING BTREE,
  INDEX `idx_task_id`(`task_id` ASC) USING BTREE,
  INDEX `idx_status`(`status` ASC) USING BTREE,
  INDEX `idx_created_time`(`created_time` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '任务执行状态表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tasks
-- ----------------------------
INSERT INTO `tasks` VALUES (1, 1, '1001', 'finished', '2025-08-23 03:00:00.000000', '2025-08-23 03:30:00.000000');
INSERT INTO `tasks` VALUES (2, 1, '1002', 'running', '2025-08-23 03:15:00.000000', NULL);
INSERT INTO `tasks` VALUES (3, 2, '2001', 'pending', '2025-08-23 04:00:00.000000', NULL);
INSERT INTO `tasks` VALUES (4, 1, '99e6131b', 'pending', '2025-08-23 13:02:55.551626', NULL);
INSERT INTO `tasks` VALUES (5, 1, 'b9a9e5ba', 'pending', '2025-08-23 13:26:36.490328', NULL);
INSERT INTO `tasks` VALUES (6, 1, '9ef58ede', 'pending', '2025-08-23 13:29:32.080638', NULL);
INSERT INTO `tasks` VALUES (7, 1, '7824e701', 'finished', '2025-08-23 13:35:10.251871', NULL);
INSERT INTO `tasks` VALUES (8, 1, '1fe293a2', 'finished', '2025-08-23 14:05:27.321942', NULL);
INSERT INTO `tasks` VALUES (9, 1, 'fb5a777c', 'finished', '2025-08-23 14:09:12.494943', NULL);
INSERT INTO `tasks` VALUES (10, 1, 'bae55ac4', 'finished', '2025-08-23 14:14:30.482340', NULL);
INSERT INTO `tasks` VALUES (11, 1, 'c8e386fb', 'finished', '2025-08-23 14:21:34.380696', NULL);
INSERT INTO `tasks` VALUES (12, 1, '8ecb182f', 'finished', '2025-08-23 19:55:26.866618', NULL);
INSERT INTO `tasks` VALUES (13, 1, 'd51097af', 'finished', '2025-08-23 20:06:43.010458', NULL);
INSERT INTO `tasks` VALUES (14, 1, '3a388f41', 'finished', '2025-08-23 20:15:03.608749', NULL);
INSERT INTO `tasks` VALUES (15, 1, '2f8fd3a1', 'finished', '2025-08-23 20:25:32.063968', NULL);
INSERT INTO `tasks` VALUES (16, 3, '73fff980', 'pending', '2025-08-26 14:41:47.229411', NULL);
INSERT INTO `tasks` VALUES (17, 3, '968026d7', 'running', '2025-08-26 14:43:27.801886', NULL);
INSERT INTO `tasks` VALUES (18, 4, '88bcdcab', 'running', '2025-08-26 14:56:19.706854', NULL);
INSERT INTO `tasks` VALUES (19, 3, 'cabebb10', 'finished', '2025-08-26 14:59:00.260875', NULL);
INSERT INTO `tasks` VALUES (20, 0, '37f9994a', 'running', '2025-08-26 15:03:49.619852', NULL);
INSERT INTO `tasks` VALUES (21, 2, 'e2374305', 'finished', '2025-08-26 15:08:56.522770', NULL);
INSERT INTO `tasks` VALUES (22, 5, '8fb0a7b5', 'running', '2025-08-26 15:10:41.497488', NULL);
INSERT INTO `tasks` VALUES (23, 5, 'ee9bb10f', 'running', '2025-08-26 15:15:55.390864', NULL);
INSERT INTO `tasks` VALUES (24, 6, 'c09b0e3a', 'running', '2025-08-26 15:20:46.884015', NULL);

SET FOREIGN_KEY_CHECKS = 1;
