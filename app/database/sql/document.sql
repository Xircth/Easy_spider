-- 文档表初始化SQL
CREATE TABLE IF NOT EXISTS `document` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` varchar(100) NOT NULL COMMENT '采集表名字',
  `table_name` varchar(100) NOT NULL COMMENT '数据存储表名',
  `count` bigint NOT NULL DEFAULT '0' COMMENT '采集数据总数',
  `comment` text COMMENT '备注',
  `source` int NOT NULL COMMENT '任务来源（任务ID）',
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) COMMENT '创建时间',
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6) COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_table_name` (`table_name`),
  KEY `idx_source` (`source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='文档表（数据采集汇总表）';

-- 插入测试数据
INSERT IGNORE INTO `document` (`name`, `table_name`, `count`, `comment`, `source`) 
VALUES 
('用户数据采集', 'user_data', 1500, '用于测试的用户数据采集任务', 1),
('商品信息采集', 'product_info', 2800, '电商平台商品信息采集', 2);