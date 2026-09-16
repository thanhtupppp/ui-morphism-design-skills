import 'package:flutter/material.dart';

class BentoExample extends StatelessWidget {
  const BentoExample({super.key});

  static const items = [
    ('Overview', 'Operations', 'Primary task and key metric receive the largest area.', true),
    ('Today', 'Energy usage', '24.8 kWh', false),
    ('Status', 'Alerts', '3 open', true),
    ('Service', 'Uptime', '99.9%', false),
  ];

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 768;
        final medium = constraints.maxWidth < 1024;
        final columns = compact ? 1 : medium ? 2 : 4;

        return GridView.builder(
          padding: EdgeInsets.all(compact ? 16 : 24),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: columns,
            crossAxisSpacing: 16,
            mainAxisSpacing: 16,
            childAspectRatio: compact ? 1.8 : 1.35,
          ),
          itemCount: items.length,
          itemBuilder: (context, index) {
            final item = items[index];
            return Card(
              clipBehavior: Clip.antiAlias,
              child: Padding(
                padding: EdgeInsets.all(compact ? 16 : 20),
                child: SingleChildScrollView(
                  primary: false,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(item.$1, style: Theme.of(context).textTheme.labelLarge),
                      const SizedBox(height: 6),
                      Text(item.$2, style: Theme.of(context).textTheme.titleLarge),
                      const SizedBox(height: 8),
                      Text(item.$3),
                      if (item.$4) ...[
                        const SizedBox(height: 16),
                        FilledButton(
                          onPressed: () {},
                          style: FilledButton.styleFrom(minimumSize: const Size(48, 48)),
                          child: Text(index == 0 ? 'Open dashboard' : 'Review alerts'),
                        ),
                      ],
                    ],
                  ),
                ),
              ),
            );
          },
        );
      },
    );
  }
}
