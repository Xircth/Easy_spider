-- 任务执行状态表初始化SQL
CREATE TABLE IF NOT EXISTS `tasks` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `task_id` int NOT NULL COMMENT '任务ID，表示一种类型的任务',
  `task_E_id` varchar(32) NOT NULL COMMENT '任务执行ID，表示任务执行的唯一标识',
  `status` varchar(20) NOT NULL DEFAULT 'pending' COMMENT '任务状态（pending, running, stop, finished）',
  `created_time` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '任务创建时间',
  `finish_time` datetime(6) NULL DEFAULT NULL COMMENT '任务完成或终止时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_task_E_id` (`task_E_id`),
  KEY `idx_task_id` (`task_id`),
  KEY `idx_status` (`status`),
  KEY `idx_created_time` (`created_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='任务执行状态表';

-- 插入测试数据（可选）
INSERT IGNORE INTO `tasks` (`task_id`, `task_E_id`, `status`, `created_time`, `finish_time`) 
VALUES 
(1, 1001, 'finished', '2025-08-23 03:00:00', '2025-08-23 03:30:00'),
(1, 1002, 'running', '2025-08-23 03:15:00', NULL),
(2, 2001, 'pending', '2025-08-23 04:00:00', NULL);