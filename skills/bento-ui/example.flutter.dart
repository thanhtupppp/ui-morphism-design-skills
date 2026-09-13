import 'package:flutter/material.dart';

class BentoExample extends StatelessWidget {
  const BentoExample({super.key});

  static const items = [
    ('Hero', 'Primary product or outcome.'),
    ('Supporting', 'Secondary information.'),
    ('Utility', 'Quick action or compact metric.'),
    ('Detail', 'A richer chart, preview, or detail module.'),
  ];

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 720;
        final columns = compact ? 1 : constraints.maxWidth >= 1024 ? 4 : 2;
        return GridView.builder(
          padding: const EdgeInsets.all(16),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: columns,
            crossAxisSpacing: 16,
            mainAxisSpacing: 16,
            mainAxisExtent: compact ? 180 : 160,
          ),
          itemCount: items.length,
          itemBuilder: (context, index) {
            final item = items[index];
            return Card(
              clipBehavior: Clip.antiAlias,
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(item.$1, style: Theme.of(context).textTheme.titleLarge),
                    const SizedBox(height: 8),
                    Expanded(child: Text(item.$2)),
                    if (index == 0)
                      FilledButton(
                        onPressed: () {},
                        style: FilledButton.styleFrom(minimumSize: const Size(44, 44)),
                        child: const Text('Open'),
                      ),
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }
}
